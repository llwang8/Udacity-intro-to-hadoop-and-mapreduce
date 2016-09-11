# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part I - Quiz: Highest Sales

def reducer():

    maxSale = 0.0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        thisSale = float(thisSale)

        if oldKey:
            if oldKey != thisKey:
                print "{0}\t{1}".format(oldKey, maxSale)
                maxSale = thisSale
                oldKey = thisKey
            else:
                if maxSale < thisSale:
                    maxSale = thisSale
        else:
            maxSale = thisSale
            oldKey = thisKey

    if oldKey != None:
        print "{0}\t{1}".format(oldKey, maxSale)






