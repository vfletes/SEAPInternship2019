#! /usr/bin/python2
desiredFile = raw_input('Would you like to find the rapid intensifying storms?\n')
if desiredFile.lower() == 'yes':
        print('Sounds good')
        fileWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_NRI_temp_list.dat', 'w')
        fileW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_temp_list.dat', 'w+')
        fileWWW = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_data.dat', 'w')
        fileRR = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_RI_list.dat', 'r')
        fileR = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_sat_ts_extracted.dat', 'r')
        print('opened')
        index = 0
        titlesRI = ['start: '] #list if RI storns to check before writing to any file
        lastCheck = False
        namez = []
        search = [] #all head lines
        rapidIntense = False #true if current storm is already on the RI list
        for line in fileR:
                if 'HEAD' in line:#puts all head lines into search
                        search.append(line)
                        i = line.split()

        for x in search:#goes through all head lines to find variables
                splitted = x.split()
                nameS = splitted[0]
                dateS = splitted[1]
                h = splitted[2]
                vmaxS = splitted[3]
                if x == search[-4]:
                        break
                if x != search[-4] or x != search[-3] or x != search[-2] or x != search[-1]: #only set comparable variables before end of file
                        Eindex = index + 4
                        lineCompare = search[Eindex]
                        spitted = lineCompare.split()
                        nameE = spitted[0]
                        dateE = spitted[1]
                        vmaxE = spitted[3]
                        if nameS == nameE:#makes sure the comparing variables are of the same storm
                                lastCheck = False
                                if int(vmaxE) - int(vmaxS) >= 30:#compares
                                        if int(dateS[:2]) < 82:
                                                for title in titlesRI:#checks if already in RI file
                                                        if nameS in title:
                                                                rapidIntense = True
                                                if rapidIntense == False:#False until added to RI
                                                        titlesRI.append(nameS)
                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 20' + str(dateS) + ' \n')
                                                        rapidIntense = True
                                                        #lastCheck = True
                                        else:
                                                for title in titlesRI:#checks if already in RI file
                                                        if nameS in title:
                                                                rapidIntense = True
                                                if rapidIntense == False:
                                                        fileW.write(str(nameS) + ' ' + str(h) + ' 19' + str(dateS) + ' \n')
                                                        titlesRI.append(nameS)
                                                        rapidIntense = True
                                                        #lastCheck = True
                        else:
                                if rapidIntense == False:#some of the nonRIs are not showing up because they are from a different date
                                        for line in fileW:
                                                if nameS in line and dS[:2] in line:
                                                        lastCheck = True
                                         if lastCheck == False:
                                                fileWW.write(str(nameS) + ' ' + str(dateS) + ' \n')
                                nameS = nameE
                                rapidIntense = False #reset no matter what
                if x != search[-1]:
                        index += 1
        for line in fileRR:
                for x in fileR:
                        if 'HEAD' in x:
                                if line[:
else:
        print('Try again with a different file')
fileWW.close()
fileWWW.close()
fileR.close()
fileRR.close()
fileW.close()
print('closed')
