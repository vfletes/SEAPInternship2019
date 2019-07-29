def setXY(fileName, stormIndex):
        global labelList
        #num += 1
        x = []
        y = []
        xLabels = []
        RI_name_data = open(fileName[:-4] +'_name' + fileName[-4:],'r') #name file
        for n in range(stormIndex):
                head_line = RI_name_data.readline()
        splitted = head_line.split() #splitting the first line of RITC names list
        marker = str(splitted[1] + splitted[2]) #getting the date and time of the RI of the TC
        markerDate = dt.datetime.strptime(marker,'%y%m%d%H')
        storm = splitted[0] #getting the name of the TC
        date = splitted[1]#beginning storm date
        stormYr = date[:2]#year of storm
        with open(fileName,'r') as RI_data:
                row = RI_data.readline()
                count = 0
                while row:
                        line = row.split()
                        sYU = line[1]
                        stormYearU = str(sYU[:2])
                        if line[-1] == 'HEAD' and line[0] == storm and stormYr == stormYearU:
                                xVar = str(line[1]) + str(line[2])
                                xLabels.append(xVar)
                                date = dt.datetime.strptime(xVar,'%y%m%d%H')
                                xVar = float(xVar)
                                #xVal = math.floor(uxVar/100.)*100. + ((uxVar/100.)%1.0)*25./.06 #uxVar was the date+hour-yearFromBeginning
                                xVal = int(date.strftime('%s')) - int(markerDate.strftime('%s'))
                                x.append(xVal)
                                if not xVal in labelList:
                                        labelList.append(xVal)
                                line2 = RI_data.readline().split()
                                y.append(int(line2[2]))
                        row = RI_data.readline()
                                #if marker in :
                                        #if num == 1:
                                                #storm1 = storm
                                                #b1 = count
                                                #x1 = xVal
                                                #y1 = int(line2[2]) + 5
                                #else:
                                #storm2 = storm
                                #b2 = count
                                #x2 = xVal
                                #y2 = int(line2[2]) + 5
                                #count += 1

        plt.plot(x,y)
        plt.xticks(labelList, np.array(labelList)/3600, rotation='vertical')
        plt.xlabel('Six Hour Increments From Rapid Intensification')
        plt.ylabel('Wind Speeds')
        plt.title( 'Storm Data')
        #plt.errorbar(x1, y1, yerr=5, label='Rapid Intensification Starts') #yerr = line height, xerr = line width
        #plt.legend()
try:
        i = 1
        while True:
                setXY('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_TC_RI.txt', i)
                i += 1
except:
        print('done')
#setXY('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_TC_RI.txt', 2)
#plt.gca().get_xticklabels()[b1].set_color('red')
#plt.gca().get_xticklabels()[b2].set_color('red')
plt.savefig('/calval_npp2/fletes/dataFiles/compositePlot.png', bbox_inches='tight')
plt.show()
