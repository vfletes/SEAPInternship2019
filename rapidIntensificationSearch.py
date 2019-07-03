#! /usr/bin/python2
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts_extracted.dat':
        print('Sounds good')
        fileR = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'w')
        print('opened')
        for line in fileR:
                if 'HEAD' in line:
                        dS = line[5:12]
                        dE = dS
                        h = line[12:15]
                        def timeIncrease():#had a global vs local error, fixed it so remember to do this!!!!!!!!!!!!
                                global dE
                                if dS[1:4] == '2':
                                        if int(dS[3:]) < 29 and dS[3:] != '29':
                                                dE = str(int(dE) + 1)
                                                if dS[0] == '0':
                                                        dE = dE.zfill(1)
                                        elif dS[3:] == '28':
                                                if int(dS[:2]) % 4 == 0:
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
                                elif dS[1:4] == '04' or dS[1:4] == '6' or dS[1:4] == '09' or dS[1:4] == '11':
                                        if int(dS[3:]) < 30:
                                                dE = str(int(dE) + 1)
                                        elif dS[3:] == '30':
                                                dE = str(int(dE) + 71)
                                        elif dS[0] == '0':
                                                dE = dE.zfill(1)
                                        return dE
                                elif dS[1:4] == '12':
                                        if int(dS[3:]) < 31:
                                                dE = str(int(dE) + 1)
                                        elif dS[3:] == '31':
                                                if dS[:2] == '99':
                                                        dE = '10101'
                                                else:
                                                        dE = str(int(dE) + 8870) # y + 1, m = 01, d + 01
                                        elif dS[0] == '0':
                                                dE = dE.zfill(1)
                                        return dE
                                else:
                                        if int(dS[3:]) < 31:
                                                dE = str(int(dE) + 1)
                                        elif dS[3:] == '31':
                                                dE = str(int(dE) + 70)
                                        elif dS[0] == '0':
                                                dE = dE.zfill(1)
                                        return dE
                        timeIncrease()
                        fileW.write('dS: ' + dS + '\n')
                        fileW.write('dE: ' + dE + '\n')
                        fileW.write('h: ' + h + '\n')
        fileR.close()
        fileW.close()
        print('closed')
else:
        print('Try again with a different file')
