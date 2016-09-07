# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part I - Quiz: Total Sales

def reducer():

    salesTotal = 0
    itemsTotal = 0


    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        thisSale = float(thisSale)

        salesTotal += thisSale
        itemsTotal += 1


    print "{0}\t{1}".format(itemslTotal, salesTotal)