#!/usr/bin/env python

from operator import itemgetter
import sys

tmax = 0
tmin = 0
maxtmx = 0
mintmn = 999999
tmaxct = 0
tminct = 0
currentyear = None
year = None
element = None
value = 0
date = None
stationid = None
hottestweatherstationsids = []
coldestweatherstationsids = []
hottestweatherstationsvalues = []
coldestweatherstationsvalues = []
hottestvalue = 0
coldestvalue = 999999
hottestday = None
coldestday = None
hottestdaystationid = None
coldestdaystationid = None



for line in sys.stdin:
    
    line = line.strip()

    date, stationid, element, value = line.split('\t', 3)
    year = str(date)[:4]

    try:
        value = int(value)
    except ValueError:
        continue

    
    if currentyear is None:
        currentyear = year

    if year == currentyear:
        if element == "TMAX":
            tmax += value
            if value > maxtmx:
                maxtmx = value
            tmaxct += 1

        elif element == "TMIN":
            tmin += value
            if value < mintmn:
                mintmn = value
            tminct += 1

        if value > hottestvalue:
            hottestvalue = value
            hottestdaystationid = stationid
            hottestday = date

        if value < coldestvalue:
            coldestvalue = value
            coldestdaystationid = stationid
            coldestday = date

        if len(hottestweatherstationsids) < 5:
            hottestweatherstationsids.append(stationid)
            hottestweatherstationsvalues.append(value)
        else:
            minhottestvalue = min(hottestweatherstationsvalues)
            if minhottestvalue < value and stationid not in hottestweatherstationsids:
                for idx, i in enumerate(hottestweatherstationsvalues):
                    if i == minhottestvalue:
                        hottestweatherstationsvalues[idx] = value
                        hottestweatherstationsids[idx] = stationid
                        break

        if len(coldestweatherstationsids) < 5:
            coldestweatherstationsids.append(stationid)
            coldestweatherstationsvalues.append(value)
        else:
            maxcoldestvalue = max(coldestweatherstationsvalues)
            if maxcoldestvalue > value and stationid not in coldestweatherstationsids:
                for idx, i in enumerate(coldestweatherstationsvalues):
                    if i == maxcoldestvalue:
                        coldestweatherstationsvalues[idx] = value
                        coldestweatherstationsids[idx] = stationid
                        break
 else:
        print '%s' % currentyear
        print 'Average TMAX\t%s\t' % (tmax * 1.0 / tmaxct)
        print 'Average TMIN\t%s\t' % (tmin * 1.0 / tminct)
        print 'Max TMAX\t%s\t' % maxtmx
        print 'Min TMIN\t%s\t' % mintmn
        print 'Hottest Weather Stations\t%s' % hottestweatherstationsids
        print 'Coldest Weather Stations\t%s' % coldestweatherstationsids

        currentyear = year
        tmax = 0
        tmin = 0
        maxtmx = 0
        mintmn = 999999
        tmaxct = 0
        tminct = 0
        hottestweatherstationsids = []
        hottestweatherstationsvalues = []
        coldestweatherstationsids = []
        coldestweatherstationsvalues = []
        if element == "TMAX":
            tmax = value
            maxtmx = value
            tmaxct = 1

        elif element == "TMIN":
            tmin = value
            mintmn = value
            tminct = 1

        
        if value < coldestvalue:
            coldestvalue = value
            coldestdaystationid = stationid
            coldestday = date
        
        if value > hottestvalue:
            hottestvalue = value
            hottestdaystationid = stationid
            hottestday = date



if year == currentyear:
    print '%s' % currentyear
    print '%s\tAverage TMAX\t%s\t' % (currentyear, (tmax * 1.0 / tmaxct))
    print '%s\tAverage TMIN\t%s\t' % (currentyear, (tmin * 1.0 / tminct))
    print '%s\tMax TMAX\t%s\t' % (currentyear, maxtmx)
    print '%s\tMin TMIN\t%s\t' % (currentyear, mintmn)
    print '%s\tHottest Weather Stations\t%s' % (currentyear, hottestweatherstationsids)
    print '%s\tColdest Weather Stations\t%s' % (currentyear, coldestweatherstationsids)
    print '\n'
    print 'Hottest Day\t%s\t - StationID\t%s' % (hottestday, hottestdaystationid)
    print 'Coldest Day\t%s\t - StationID\t%s' % (coldestday, coldestdaystationid)


                                                                                                                                                                                       1,1           Top
