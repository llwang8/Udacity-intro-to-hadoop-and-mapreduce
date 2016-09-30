
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
#Combine Datasets

def mapper(strlist):
    #reader = csv.reader(sys.stdin, delimiter='\t')
    #writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    forumdata = []
    #for line in reader:
    for line in strlist:
        line = line.strip().split('\t')
        if len(line) == 5:
            #user_id, reputation, gold, silver, bronze = data
            data = [line[0], "A", line[1], line[2], line[3], line[4]]
        if len(line) == 9:
            #nid, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_str, last_edited_id, last_act_by_id, last_act_at, active_rev_id, extra, extra_ref_id, extra_count, marked = data
            data = [line[3], "B", line[0],line[1],line[2],line[4],line[5],line[6],line[7], line[8]]

        #writer.writerow(forumdata)
        forumdata.append(",".join(data))
    reducer(forumdata)

def reducer(datalist):
    user = []
    forum = []
    oldKey = None
    #for line in sys.stdin:
    for line in datalist:
        data_mapped = line.strip().split(',')
        #print data_mapped
        if oldKey is None or oldKey != data_mapped[0]:
            oldKey = data_mapped[0]

        if len(data_mapped) == 6:
            user = data_mapped
            #print user
        elif len(data_mapped) == 10:
            forum = data_mapped
            #print forum
        else:
            continue

    if user and forum:
        print forum[2:] + user[2:]


stringList = ['12345\t11\t3\t4\t1',
'6336\tUnit 1: Same Value Q\tcs101 value same\t12345\tquestion\t\N\t\N\t2012-02-25 08:09:06.787181+00\t1']

print mapper(stringList)




