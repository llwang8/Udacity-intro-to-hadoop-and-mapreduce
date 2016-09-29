# -------------------------------------#
# Intro to Hadoop and MapReduce        #
# Lesson 4: MapReduce Design Pattern   #
# -------------------------------------#
# Quiz: Finding Mean

#!/usr/bin/python

from datetime import datetime
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)



def reducer():
    sales_by_weekday = {}

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")

        if len(data_mapped) != 2:
            continue

        weekday, sales = data_mapped
        sales = float(sales)

        sales_summary = sales_by_weekday.get(weekday, {'sum': 0, 'count': 0})  # using get to provide a default if not exists
        sales_summary['sum'] += sales
        sales_summary['count'] += 1
        sales_by_weekday[weekday] = sales_summary

    for wk in sales_by_weekday:
        print "{0}\t{1}".format(wk, sales_by_weekday[wk]['sum'] / sales_by_weekday[wk]['count'])



purchases = ['2012-01-01\t09:00\tSan Jose\tMens clothing\t214.05\tAmex',
                '2012-01-01\t09:00\tFort Worth\tWomen clothing\t15.57\tVisa'
            ]

