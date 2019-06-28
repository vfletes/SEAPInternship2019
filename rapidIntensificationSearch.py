#! /usr/bin/python2
h = 12
desiredFile = raw_input('Which file would you like to search? ')
if desiredFile == 'REDUCED_AL_SHIPS_1982_2017_sat_ts.dat':
        print('Sounds good')
        fileR = open('/users/fletes/dataFiles/REDUCED_AL_SHIPS_1982_2017_sat_ts.dat', 'r')
        fileRW = open('/users/fletes/dataFiles/RAPID_REDUCED_AL_SHIPS_1982_2017_sat_ts.dat', 'w')
        fileNRW = open('/users/fletes/dataFiles/NONRAPID_REDUCED_AL_SHIPS_1982_2017_sat_ts.dat', 'w')
        print('opened')
        print('I'm making a comment')
        print(windowS)
        print(windowE)
        #for line in fileR:  might have to go about this another way
        fileR.close()
        fileRW.close()
        fileNRW.close()
        print('closed')
else:
        print('Try again with a different file')
def timeIncrease():
        if int(dS[2:4]) == 2:
                if int(dS[4:6]) < 29 and int(dS[10:12]) != 29:
                        dE = str(int(dE) + 1)
                        if dS[0] == 0:
                                dE = dE.zfill(1)
                elif int(dS[2:4]) == 28:
                        if int(dS(0:2) % 4 == 0:
                                leapYear = True
                                dE = str(int(dE) + 1)
                        elif dS[0] == 0:
                                dE = dE.zfill(1)
                else:
                        dE = str(int(dE) + 100)
                        if leapYear == True:
                                dE = str(int(dE) - 28)
                        elif leapYear == False:
                                dE = str(int(dE) - 27)
                        elif dS[0] == 0:
                                dE = dE.zfill(1)
        elif int(dS[2:4]) == 4 or int(dS[2:4]) == 6 or int(dS[2:4]) == 9 or int(dS[2:4]) == 11:
                if int(dS[4:6]) < 30:
                        dE = str(int(dE) + 1)
                elif int(dS[4:6]) == 30:
                        dE = str(int(dE) + 71)
                elif dS[0] == 0:
                        dE = dE.zfill(1)
        elif int(dS[2:4]) == 12:
                if int(dS[4:6]) < 31:
                        dE = str(int(dE) + 1)
                elif int(dS[4:6]) == 31:
                        if int(dS[0:2]) == 99:
                                dE = str('10101').zfill(1)
                        else:
                                dE = str(int(dE) + 8870) # y + 1, m = 01, d + 01
                elif dS[0] == 0:
                        dE = dE.zfill(1)
        else:
                if int(dS[4:6]) < 31:
                        dE = str(int(dE) + 1)
                elif int(dS[4:6]) == 31:
                        dE = str(int(dE) + 70)
                elif if dS[0] == 0:
                        dE = dE.zfill(1)
