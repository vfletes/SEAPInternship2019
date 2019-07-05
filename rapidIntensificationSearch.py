#! /usr/bin/python2
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts_extracted.dat':
        print('Sounds good')
        fileR = open('/calval_npp2/fletes/dataFiles/practiceData.dat', 'r')
        fileWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_NRI_list.dat', 'w')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'w')
        print('opened')
        firstLine = fileR.readline()
        nameS = firstLine[1:5]
        velocityA = False
        velocityB = False
        for line in fileR:
                #line = fileR.read().splitlines()
                if 'HEAD' in line:
                        global nameE
                        global dE
                        global h
                        nameE = line[1:5]
                        dS = line[6:12]
                        dE = dS
                        h = line[12:15]
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
                                                elif dS[0] == '0':
                                                        dE = dE.zfill(1)
                                        else:
                                                dE = str(int(dE) + 100)
                                                if leapYear == True:
                                                        dE = str(int(dE) - 28)
                                                elif leapYear == False:
                                                        dE = str(int(dE) - 27)
                                                elif dS[0] == '0':
                                                        dE = dE.zfill(1)
                                        return dE
                                elif dE[2:4] == '04' or dE[2:4] == '06' or dE[2:4] == '09' or dE[2:4] == '11':
                                        if int(dE[4:]) < 30:
                                                dE = str(int(dS) + 1)
                                        elif dE[4:] == '30':
                                                dE = str(int(dE) + 71)
                                        elif dE[0] == '0':
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
                                        elif dS[0] == '0':
                                                dE = dE.zfill(1)
                                         return dE
                                else:
                                        if int(dE[4:]) < 31:
                                                dE = str(int(dS) + 1)
                                        elif dE[4:] == '31':
                                                dE = str(int(dS) + 70)
                                        elif dS[0] == '0':
                                                dE = dE.zfill(1)
                                        return dE
                        timeIncrease()
                        if nameS == nameE:
                                for li in fileR:
                                        fileW.write(li)
                                        #enters here
                                        if 'HEAD' in li:
                                                print('found head')
                                                if h in li:
                                                        print('h found')
                                                        if nameS in li:
                                                                if dS in li:
                                                                        l = li + 1
                                                                        splitted = l.split()
                                                                        vS = splitted[2]
                                                                        velocityA = True
                                                                        print('dS found')
                                                                elif dE in lines:
                                                                        ll = li + 1
                                                                        splitt = ll.split()
                                                                        vE = splitt[2]
                                                                        velocityB = True
                                                                        print('dE found')
                                                                if velocityA == True and velocityB == True:
                                                                        print('both velocities are set to true')
                                                                        if vE - vS == 30:
                                                                                if int(dS[:2]) < 82:
                                                                                        #fileW.write(nameS + ' ' + h + ' 20', dS)
                                                                                        print('reachedA')
                                                                                else:
                                                                                        #fileW.write(nameS + ' ' +  h + ' 19', dS)
                                                                                        print('reachedB')
                                                                                break
                        else:
                                #fileWW.write(nameS)
                                nameS = nameE
        fileR.close()
        fileWW.close()
        fileW.close()
        print('closed')
else:
        print('Try again with a different file')
