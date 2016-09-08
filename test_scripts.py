

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

        if oldKey and oldKey != thisKey:
            if hitsMax < hitsTotal:
                hitsMax = hitsTotal
                pathMax = thisKey
            hitesTotal = 0

        oldKey = thisKey
        hitsTotal += 1


    print "{0}\t{1}".format(pathMax, hitsMax)

paths = [
        'http://www.the-associates.co.uk/15.223.157.186',
        '13.223.157.186',
        '15.223.157.186',
        'http://www.the-associates.co.uk16.223.157.186',
        'http://www.the-associates.co.uk/17.223.157.186',
        'http://www.the-associates.co.uk17.223.157.186',
        '17.223.157.186',
        '18.223.157.186']

print reducer2(paths)
