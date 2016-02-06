# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:59:13 2016

@author: gaurav_sathe
"""

import json
import os

cwd = "gdis_eventMentions"

allDocs = os.listdir(cwd)

esIndex = open("esIndex.txt","w")

_index = "allevents"
_type = "eventmention"
_id = 0

i = 0

for document in allDocs :

    allEvents = open(cwd + "/" + document).readlines()

    for event in allEvents :
        _id = _id + 1
        index = {"index" :
                    {
                        "_index" : _index,
                        "_type" : _type,
                        "_id" : str(_id)
                    }
                }

        esIndex.write(json.dumps(index) + "\n")
        esIndex.write(event)

    i = i+1

    if i % 500 == 0 :
        print i

esIndex.close()