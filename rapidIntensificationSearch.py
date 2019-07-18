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
if desiredFile.lower() == 'yes':
        print('Sounds good')
        fileRR = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r')
        fileWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_NRI_list.dat', 'w')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'w')
        print('opened')
        firstLine = fileRR.readline()
        nameS = firstLine[1:5]
        rapidIntense = False
        dEtruth = False
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
                                vS = spitted[3]
                                timeIncrease()
                                lineee = fileR.readline()
                                splitted = lineee.split()
                                vS = splitted[2]
                                with open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r') as fileRRR:
                                        linee = fileRRR.readline()
                                        if nameS == nameE:
                                                while linee:
                                                        if dEtruth == True:
                                                                break
                                                        else:
                                                                if 'HEAD' in linee:
                                                                        if h in linee:
                                                                                if nameS in linee:
                                                                                        if dE in linee:
                                                                                                splitt = linee.split()
                                                                                                vE = splitt[3]
                                                                                                dEtruth = True
                                                        linee = fileRRR.readline()
                                                if int(vE) - int(vS) >= 30:
                                                        if int(dS[:2]) < 82:
                                                                if rapidIntense == False:
                                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 20' + str(dS) + ' \n')
                                                                rapidIntense = True
                                                                dEtruth = False
                                                                velocityA = False
                                                                velocityB = False
                                                        else:
                                                                if rapidIntense == False:
                                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 19' + str(dS) + ' \n')
                                                                rapidIntense = True
                                                                dEtruth = False
                                                                velocityA = False
                                                                velocityB = False
                                        else:
                                                if rapidIntense == False:
                                                        fileWW.write(str(nameS) + ' ' + str(dS) + ' \n')
                                                nameS = nameE
                                                nameE = nameS
                                                rapidIntense = False
                        line = fileR.readline()
else:
        print('Try again with a different file')
fileRR.close()
fileWW.close()
fileR.close()
fileW.close()
fileRRR.close()
print('closed')
