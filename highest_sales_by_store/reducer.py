# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part I - Quiz: Highest Sales

def reducer():

    maxSale = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        thisSale = float(thisSale)


        if maxSale < thisSale:
            maxSale = thisSale

        if oldKey and oldKey != thisKey:
            if oldKey != None:
                print "{0}\t{1}".format(oldKey, maxSale)
            maxSale = 0

        oldKey = thisKey

    if oldKey != None:
        print "{0}\t{1}".format(oldKey, maxSale)
