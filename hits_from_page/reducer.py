# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part II - Quiz: Hits from Page

def reducer():

    hitsTotal = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip()

        if data is None:
            continue
        thisKey = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, hitsTotal)
            hitsTotal = 0

        oldKey = thisKey
        hitsTotal += 1


print "{0}\t{1}".format(oldKey, hitsTotal)