# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#


def reducer(list):

    maxSale = 0
    oldKey = None

    #for line in sys.stdin:
    #    data = line.strip().split("\t")

    for e in list:

        thisKey = e[0]
        thisSale = e[1]

        if oldKey and oldKey == thisKey:
            if maxSale < thisSale:
                maxSale = thisSale
        else:
            if oldKey != None:
                print "{0}\t{1}".format(oldKey, maxSale)
            maxSale = thisSale
            oldKey = thisKey

    if oldKey != None:
        print "{0}\t{1}".format(oldKey, maxSale)

library = [['a': 10], ['a': 120], ['a': 66], ['b': 30], ['b': 99], ['b': 150], ['c': 60], ['c': 90]]

print reducer(library)
