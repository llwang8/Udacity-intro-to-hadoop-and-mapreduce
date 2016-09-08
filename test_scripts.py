

def reducer(lib):

    hitsTotal = 0
    oldKey = None

    #for line in sys.stdin:
    for line in lib:
        data = line.strip()

        if len(data) != 1:
            continue
        thisKey = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, hitsTotal)
            hitsTotal = 0

        oldKey = thisKey
        hitsTotal += 1

        print "{0}\t{1}".format(oldKey, hitsTotal)

library = ['10.223.157.186', '12.223.157.186', '13.223.157.186', '14.223.157.186', '15.223.157.186', '16.223.157.186', '17.223.157.186', '18.223.157.186']

print reducer(library)

def reducer2(paths):

    hitsTotal = 0
    hitsMax = 0
    pathMax = ''
    oldKey = None

    #for line in sys.stdin:
    for line in paths:
        data = line.strip()

        if data is None:
            continue
        thisKey = data.replace('http://www.the-associates.co.uk', '')
        print 'thisKey: ' + thisKey

        if oldKey and oldKey != thisKey:
            print "oldKey: " + oldKey + "\t hitsTotal: " + str(hitsTotal)
            if hitsMax < int(hitsTotal):
                hitsMax = hitsTotal
                pathMax = oldKey
            hitsTotal = 0
            print "pathMax: " + pathMax + "\t hitsMax: " + str(hitsMax)

        oldKey = thisKey
        hitsTotal += 1


    print "{0}\t{1}".format(pathMax, hitsMax)

paths = [
        '/13.223.157.186',
        'http://www.the-associates.co.uk/15.223.157.186',
        '/15.223.157.186',
        'http://www.the-associates.co.uk/16.223.157.186',
        'http://www.the-associates.co.uk/17.223.157.186',
        'http://www.the-associates.co.uk/17.223.157.186',
        '/17.223.157.186',
        '/18.223.157.186']

print reducer2(paths)
