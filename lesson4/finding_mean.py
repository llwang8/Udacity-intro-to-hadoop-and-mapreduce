# -------------------------------------#
# Intro to Hadoop and MapReduce        #
# Lesson 4: MapReduce Design Pattern   #
# -------------------------------------#
# Quiz: Finding Mean
from datatime import datatime
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(date, cost)



def reducer():
    sales_by_weekday = {}

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")

        if len(data_mapped) != 2:
            continue

        date, sales = data_mapped
        weekday = datetime.strptime(date, "%y-%m-%d").weekday()
        sales = float(sales)

        sales_summary = sales_by_weekday.get(weekday, {'sum': 0, 'count': 0})
        sales_summary['sum'] += sales
        sales_summary['count'] += 1
        sales_by_weekday[weekday] = sales_summary

    for wk in sales_by_weekday:
        print "{0}\t{1}".format(wk, sales_by_weekday[wk]['sum'] / sales_by_weekday[wk]['count'])






