# -------------------------------------#
# Intro to Hadoop and MapReduce        #
# Lesson 4: MapReduce Design Pattern   #
# -------------------------------------#
# Quiz: Combine Datasets

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    forumdata = []
    for line in reader:
        line = line.strip().split('\t')
        if len(line) == 5:
            #user_id, reputation, gold, silver, bronze = data
            forumdata = [line[0], "A", line[1], line[2], line[3], line[4]]
        if len(line) == 19:
            #nid, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_str, last_edited_id, last_act_by_id, last_act_at, active_rev_id, extra, extra_ref_id, extra_count, marked = data
            forumdata = [line[3], "B", line[0],line[1],line[2],line[5],line[6],line[7],line[8], line[9]]

        writer.writerow(forumdata)

def reducer():
    user = []
    forum = []
    oldKey = None
    for line in sys.stdin:
        data_mapped = line.strip().split(',')
        if oldKey is None or oldKey != data_mapped[0]:
            oldKey = data_mapped[0]
            user = []
            forum = []

        if len(data_mapped) == 6:
            user = data_mapped
        elif len(data_mapped) == 10:
            forum = data_mapped
        else:
            continue

        if user and forum:
            writer.writrow(form[2:] + user[2:])




