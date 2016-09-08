# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part II - Quiz: Most Popular

def reducer():

    hitsTotal = 0
    hitsMax = 0
    pathMax = ''
    oldKey = None

    for line in sys.stdin:
        data = line.strip()

        if data is None:
            continue
        #thisKey = data.replace('http://www.the-associates.co.uk', '')
        thisKey = data

        if oldKey and oldKey != thisKey:
            if hitsMax < hitsTotal:
                hitsMax = hitsTotal
                pathMax = oldKey
            hitsTotal = 0

        oldKey = thisKey
        hitsTotal += 1


    print "{0}\t{1}".format(pathMax, hitsMax)