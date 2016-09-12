# -------------------------------------#
# Intro to Hadoop and MapReduce        #
# Lesson 4: MapReduce Design Pattern   #
# -------------------------------------#
# Quiz: Inverted Index

import sys
import re
import string

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 19:
            continue

        nid, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_str, last_edited_id, last_act_by_id, last_act_at, active_rev_id, extra, extra_ref_id, extra_count, marked = data
        if nid != '"id"':  #get rid of title row
            print "{0}\t{1}".format(nid, body)


def reducer():
    wordlib = {}

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')


        if len(data_mapped) != 2:
            continue

        nid, body = data_mapped

        nid = int(string.replace(nid, '"', '', 2)) #take out nodeid double quotes and change it to int

        cleanr = re.compile('<.*?>')
        body = re.sub(cleanr, '' , body)  #take out html tags
        wordlist =  re.split(r'[.,!?:;\"()<>\[\]#$=\-/\s"]\s*', body) #multiple dilimenators

        for word in wordlist:
            nodelist = wordlib.get(word, []) #add default []
            nodelist.append(nid)
            wordlib[word] = sorted(nodelist) #sort nodelist ascending

    for key in wordlib:
        print "{0}\t{1}".format(key, wordlib[key])

    print 'fantastic' + '\t' + wordlib['fantastic']



