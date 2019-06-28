#! /usr/bin/python2
desiredFile = raw_input('Which file would you like to reduce? ')
if desiredFile == 'AL_SHIPS_1982_2017_sat_ts.dat':
        print('Sounds good')
        fileR = open('/users/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts.dat', 'r')
        fileW = open('/users/fletes/dataFiles/REDUCED_AL_SHIPS_1982_2017_sat_ts.dat', 'w')
        print('opened')
        for line in fileR:
                if 'PW' in line:
                        fileW.write(line)
                elif 'RH' in line:
                        fileW.write(line)
                elif ' LAT' in line:
                        fileW.write(line)
                elif ' LON' in line:
                        fileW.write(line)
                elif 'DTL' in line:
                        fileW.write(line)
                elif 'NSST' in line:
                        fileW.write(line)
                elif 'HEAD' in line:
                        fileW.write(line)
                elif 'VMAX' in line:
                        fileW.write(line)
                elif 'MSLP' in line:
                        fileW.write(line)
                elif 'COHC' in line:
                        fileW.write(line)
                elif 'DSTA' in line:
                        fileW.write(line)
                elif 'Z850' in line:
                        fileW.write(line)
                elif 'D200' in line:
                        fileW.write(line)
                elif 'TADV' in line:
                        fileW.write(line)
                elif 'SHRD' in line:
                        fileW.write(line)
                elif 'SHTD' in line:
                        fileW.write(line)
                elif 'SHRS' in line:
                        fileW.write(line)
                elif 'SHTS' in line:
                        fileW.write(line)
                elif 'SHRG' in line:
                        fileW.write(line)
        fileR.close()
        fileW.close()
        print('closed')
else:
        print('Incorrect, try again with a different document')
