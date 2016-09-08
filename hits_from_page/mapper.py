# -------------------------------#
# Intro to Hadoop and MapReduce  #
# Lesson 3: MapReduce Project    #
# -------------------------------#
# Part II - Quiz: Hits from Page
#
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")

        if len(data) != 10:
            continue

        ip, clientID, user, time1, time2, request, path, protocol, status, return_size = data
        print "{0}".format(ip)

def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__