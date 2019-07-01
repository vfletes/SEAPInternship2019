#! /usr/bin/python2
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts_extracted.dat':
        print('Sounds good')
        fileR = open('/users/fletes/dataFiles/practiceData.dat', 'r')
        fileW = open('/users/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_listed.dat', 'w')
        print('opened')
        for line in fileR:
                if 'HEAD' in line:
                        dS = line[6:12]
                        dE = dS
                        h = line[13:15]
                        def timeIncrease():
                                if int(dS[2:4]) == 2:
                                        if int(dS[4:6]) < 29 and int(dS[10:12]) != 29:
                                                dE = str(int(dE) + 1)
                                                if int(dS[0]) == 0:
                                                        dE = dE.zfill(1)
                                        elif int(dS[2:4]) == 28:
                                                if int(dS[0:2]) % 4 == 0:
                                                        leapYear = True
                                                        dE = str(int(dE) + 1)
                                                elif int(dS[0]) == 0:
                                                        dE = dE.zfill(1)
                                        else:
                                                dE = str(int(dE) + 100)
                                                if leapYear == True:
                                                        dE = str(int(dE) - 28)
                                                elif leapYear == False:
                                                        dE = str(int(dE) - 27)
                                                elif int(dS[0]) == 0:
                                                        dE = dE.zfill(1)
                                elif int(dS[2:4]) == 4 or int(dS[2:4]) == 6 or int(dS[2:4]) == 9 or int(dS[2:4]) == 11:
                                        if int(dS[4:6]) < 30:
                                                dE = str(int(dE) + 1)
                                        elif int(dS[4:6]) == 30:
                                                dE = str(int(dE) + 71)
                                        elif int(dS[0]) == 0:
                                                dE = dE.zfill(1)
                                elif int(dS[2:4]) == 12:
                                        if int(dS[4:6]) < 31:
                                                dE = str(int(dE) + 1)
                                        elif int(dS[4:6]) == 31:
                                                if int(dS[0:2]) == 99:
                                                        dE = str(10101).zfill(1)
                                                else:
                                                        dE = str(int(dE) + 8870) # y + 1, m = 01, d + 01
                                        elif int(dS[0]) == 0:
                                                dE = dE.zfill(1)
                                else:
                                        if int(dS[4:6]) < 31:
                                                dE = str(int(dE) + 1)
                                        elif int(dS[4:6]) == 31:
                                                dE = str(int(dE) + 70)
                                        elif int(dS[0]) == 0:
                                                dE = dE.zfill(1)
                        if dS == dE:
                                timeIncrease()
                                print('dS: ' + dS)
                                print('dE: ' + dE)
                                print('h: ' + h)
        fileR.close()
        fileRW.close()
        fileNRW.close()
        print('closed')
else:
        print('Try again with a different file')
