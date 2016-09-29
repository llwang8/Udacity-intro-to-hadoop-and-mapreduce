# -------------------------------------#
# Intro to Hadoop and MapReduce        #
# Lesson 4: MapReduce Design Pattern   #
# -------------------------------------#
# Quiz: Combiners

from datatime import datatime
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)



def reducer():
    sales_by_weekday = {}

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")

        if len(data_mapped) != 2:
            continue

        weekday, thisSale = data_mapped
        thisSale = float(thisSales)

        sales_list = sales_by_weekday.get(weekday, [])
        sales_list.append(thisSale)
        sales_by_weekday[weekday] = sales_list

    for wk in sales_by_weekday:
        print "{0}\t{1}".format(wk, sum(sales_by_weekday[wk]) / len(sales_by_weekday[wk]))


