#! /usr/bin/python2
def timeIncrease():
        global dE
        if dE[2:4] == '02':
                if int(dE[4:]) < 29 and dE[4:] != '29':
                        dE = str(int(dE) + 1)
                        if dS[0] == '0':
                                dE = dE.zfill(1)
                elif dE[4:] == '28':
                        if int(dE[:2]) % 4 == 0:
                                leapYear = True
                                dE = str(int(dE) + 1)
                        if dS[0] == '0':
                                dE = dE.zfill(1)
                else:
                        if leapYear == True:
                                dE = str(int(dE) + 72)
                        elif leapYear == False:
                                dE = str(int(dE) + 73)
                        if dS[0] == '0':
                                dE = dE.zfill(1)
                return dE
        elif dE[2:4] == '04' or dE[2:4] == '06' or dE[2:4] == '09' or dE[2:4] == '11':
                if int(dE[4:]) < 30:
                        dE = str(int(dS) + 1)
                elif dE[4:] == '30':
                        dE = str(int(dE) + 71)
                if dS[0] == '0':
                        dE = dE.zfill(1)
                return dE
        elif dE[2:4] == '12':
                if int(dE[4:]) < 31:
                        dE = str(int(dE) + 1)
                elif dE[4:] == '31':
                        if dE[:2] == '99':
                                dE = '10101'
                        else:
                                dE = str(int(dE) + 8870) #y + 1, m = 01, d + 01
                if dS[0] == '0':
                        dE = dE.zfill(1)
                return dE
        else:
                if int(dE[4:]) < 31:
                        dE = str(int(dS) + 1)
                elif dE[4:] == '31':
                        dE = str(int(dS) + 70)
                if dS[0] == '0':
                        dE = dE.zfill(1)
                return dE
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts_extracted.dat':
        print('Sounds good')
        fileRR = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r')
        fileWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_NRI_list.dat', 'w')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'w')
        print('opened')
        firstLine = fileRR.readline()
        nameS = firstLine[1:5]
        velocityA = False
        velocityB = False
        last_pos = 1
        #rapidIntense = False
        with open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r') as fileR:
                line = fileR.readline()
                while line:
                        if 'HEAD' in line:
                                global nameE
                                global dE
                                global h
                                spitted = line.split()
                                nameE = spitted[0]
                                dS = spitted[1]
                                dE = dS
                                h = spitted[2]
                                timeIncrease()
                                with open('/calval_npp2/fletes/dataFiles/practiceData.dat', 'r') as fileRRR:
                                        number = 1
                                        linee = fileRRR.readline()
                                        if nameS == nameE:
                                                        #rapidIntense = False
                                                while linee:
                                                        linee = fileRRR.readline()
                                                        if 'HEAD' in linee:
                                                                if h in linee:
                                                                        if nameS in linee:
                                                                                if dS in linee:
                                                                                        last_pos = fileRRR.tell()
                                                                                        lineee = fileRRR.readline()
                                                                                        splitted = lineee.split()
                                                                                        vS = splitted[2]
                                                                                        velocityA = True
                                                                                        fileRRR.seek(last_pos)
                                                                                elif dE in linee:
                                                                                        last_poss = fileRRR.tell()
                                                                                        lineee = fileRRR.readline()
                                                                                        splitt = lineee.split()
                                                                                        vE = splitt[2]
                                                                                        velocityB = True
                                                                                        fileRRR.seek(last_poss)
                                                if velocityA == True and velocityB == True:
                                                        if int(vE) - int(vS) >= 30:
                                                                if int(dS[:2]) < 82:
                                                                        #if rapidIntense == False:
                                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 20' + str(dS) + ' \n')
                                                                        print('reachedA')
                                                                                #rapidIntense = True
                                                                        velocityA = False
                                                                        velocityB = False

                                                                else:
                                                                        #if rapidIntense == False:
                                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 19' + str(dS) + ' \n')
                                                                        print('reachedB')
                                                                                #rapidIntense = True
                                                                        velocityA = False
                                                                        velocityB = False
                                        else:
                                                #if rapidIntense == False:
                                                fileWW.write(nameS + ' \n')
                                                nameS = nameE
                                                #rapidIntense = False
                                line = fileR.readline()
        fileRR.close()
        fileWW.close()
        fileR.close()
        fileW.close()
        fileRRR.close()
        print('closed')
else:
        print('Try again with a different file')
#work hard but know when to take breaks, draw people out in life, follow fitness accounts and draw those bodies to learn anatomy, humana.com is a great resource to draw real people, if struggling with same face syndrome change the face
#shape, nose shape, and eyebrow shase
