#! /usr/bin/python2 im so very tired
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts_extracted.dat':
        print('Sounds good')
        fileRR = open('/calval_npp2/fletes/dataFiles/practiceData.dat', 'r')
        fileWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_NRI_list.dat', 'w')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'w')
        print('opened')
        firstLine = fileRR.readline()
        nameS = firstLine[1:5]
        velocityA = False
        velocityB = False
        number = 1
        last_pos = 1
        #numba = 1
        with open('/calval_npp2/fletes/dataFiles/practiceData.dat', 'r') as fileR:
                line = fileR.readline()
                while line:
                        #print(line)
                        #last_posss = fileR.tell()
                        #fileR.seek(last_pos)
                        #line = fileR.readline()
                        #numba += 1
                        if 'HEAD' in line:
                                #print('outer head')
                                global nameE
                                global dE
                                global h
                                spitted = line.split()
                                nameE = spitted[0]
                                print('nameE: ' + nameE)
                                dS = spitted[1]
                                print('dS: ' + dS)
                                dE = dS
                                h = spitted[2]
                                print('h: ' + h)
                                def timeIncrease():#works great, so proud of this section ahfhdhs
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
                                timeIncrease()
                                with open('/calval_npp2/fletes/dataFiles/practiceData.dat', 'r') as fileRRR:
                                        if nameS == nameE:
                                                fileRRR.seek(number)
                                                linee = fileRRR.readline()
                                                print('outside linee: ' + linee)
                                                while linee:
                                                        #fileRRR.seek(number)
                                                        linee = fileRRR.readline()
                                                        if number < 1:
                                                                print('inside: ' + linee)
                                                        number += 1
                                                        if 'HEAD' in linee:
                                                                #fileW.write(linee)
                                                                if h in linee:
                                                                        #print('h found: ' + h)
                                                                        if nameS in linee:
                                                                                if dS in linee:
                                                                                        #print('dS found: ' + dS)
                                                                                        #number += 1
                                                                                        last_pos = fileRRR.tell()
                                                                                        lineee = fileRRR.readline()
                                                                                        splitted = lineee.split()
                                                                                        vS = splitted[2]
                                                                                        #print('vmax vS: ' + vS)
                                                                                        velocityA = True
                                                                                        fileRRR.seek(last_pos)
                                                                                if dE in linee:
                                                                                        #print('dE found: ' + dE)
                                                                                        #number += 1
                                                                                        last_poss = fileRRR.tell()
                                                                                        lineee = fileRRR.readline()
                                                                                        splitt = lineee.split()
                                                                                        vE = splitt[2]
                                                                                        #print('vmax vE: ' + vE)
                                                                                        velocityB = True
                                                                                        fileRRR.seek(last_pos)
                                                                if velocityA == True and velocityB == True:
                                                                        print('both velocities are set to true')
                                                                        if int(vE) - int(vS) >= 30:
                                                                                if int(dS[:2]) < 82:
                                                                                        #fileW.write(nameS + ' ' + h + ' 20', dS)
                                                                                        print('reachedA')
                                                                                        velocityA = False
                                                                                        velocityB = False
                                                                                else:
                                                                                        #fileW.write(nameS + ' ' + h + ' 19', dS)
                                                                                        print('reachedB')
                                                                                        #print(linee)
                                                                                        velocityA = False
                                                                                        velocityB = False
                                                                #elif velocityA == True or velocityB == True:
                                                                #       linee = fileRRR.readline()
                                        else:
                                                #fileWW.write(nameS)
                                                #only uncomment the line above when it is finished and ready to run for real
                                                nameS = nameE
                                #numba += 1
                                #line.seek(numba)
                                #line = fileR.readline()
                                print('out')
        fileRR.close()
        fileWW.close()
        fileR.close()
        fileW.close()
        fileRRR.close()
        print('closed')
else:
        print('Try again with a different file')
