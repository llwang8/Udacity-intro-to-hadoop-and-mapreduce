
#====================================
def reducer(lib):

    hitsTotal = 0
    oldKey = None

    #for line in sys.stdin:
    for line in lib:
        data = line.strip()

        if len(data) != 1:
            continue
        thisKey = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, hitsTotal)
            hitsTotal = 0

        oldKey = thisKey
        hitsTotal += 1

        print "{0}\t{1}".format(oldKey, hitsTotal)

library = ['10.223.157.186', '12.223.157.186', '13.223.157.186', '14.223.157.186', '15.223.157.186', '16.223.157.186', '17.223.157.186', '18.223.157.186']

print reducer(library)

def reducer2(paths):

    hitsTotal = 0
    hitsMax = 0
    pathMax = ''
    oldKey = None

    #for line in sys.stdin:
    for line in paths:
        data = line.strip()

        if data is None:
            continue
        thisKey = data.replace('http://www.the-associates.co.uk', '')
        print 'thisKey: ' + thisKey

        if oldKey and oldKey != thisKey:
            print "oldKey: " + oldKey + "\t hitsTotal: " + str(hitsTotal)
            if hitsMax < hitsTotal:
                hitsMax = hitsTotal
                pathMax = oldKey
            hitsTotal = 0
            print "pathMax: " + pathMax + "\t hitsMax: " + str(hitsMax)

        oldKey = thisKey
        hitsTotal += 1


    print "{0}\t{1}".format(pathMax, hitsMax)

paths = [
        '/13.223.157.186',
        'http://www.the-associates.co.uk/15.223.157.186',
        '/15.223.157.186',
        'http://www.the-associates.co.uk/16.223.157.186',
        'http://www.the-associates.co.uk/17.223.157.186',
        'http://www.the-associates.co.uk/17.223.157.186',
        '/17.223.157.186',
        '/18.223.157.186']

print reducer2(paths)


#====================================
import re

#print re.split(r'[.,;!?\s]+', 'This,is;  a,; string.a ,d b.c? d!e')
#print re.split(r'[.,;;!?()<>#$=/\[\]\-\"\s]+', 'a, b.c? d!e f: g; h(k)lo"p#q$r=s-t/u[v]w')
#print re.split(r'[.,!?:;\"()<>\[\]#$=\-/\s"]\s*', 'a, b.c? d!e : f;  g(h>i<j[kkk<  ')

def reducer(lib):
    wordlib = {}

    #for line in sys.stdin:
    for line in lib:
        cleanr = re.compile('<.*?>')
        line = re.sub(cleanr, '' , line)

        #nid, body = data_mapped
        nid = 3

        #print 'line: ' + line
        wordlist =  re.split(r'[.,!?:;\"()<>\[\]#$=\-/\s"]\s*', line)
        #print wordlist

        for word in wordlist:
            nid = int(nid) + 1
            nodelist = wordlib.get(word, [])
            nodelist.append(nid)
            wordlib[word] = sorted(nodelist)

    print wordlib
    for key in wordlib:
        print "{0}\t{1}".format(key, wordlib[key])

    #print 'fantastic' + '\t' + wordlib['fantastic']


library = ['<p>a, b.c? </p>d!e : f;  g(h[kkk<  ', 'g,/d/g= g= g= h- h: m], n r$a ', 'a!b=c-d/</f>']
print reducer(library)


#====================================




