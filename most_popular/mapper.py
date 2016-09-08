# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part II - Quiz: Most Popular
#
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")

        if len(data) != 10:
            continue

        ip, clientID, user, time1, time2, request, path, protocol, status, return_size = data
        print "{0}\t{1}".format(request)

def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__