# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:39:42 2016

@author: gaurav_sathe
"""

import json
import os
from extractElements import extractElements
from extractArguments import extractArguments
import time

cwd = "gdis"

allDocs = os.listdir(cwd)

i = 0

t1 = time.time()

for document in allDocs :
    
    # Load document
    doc = json.loads(open(cwd + "\\" + document, "r").read())
    
    # Check if document has events
    events = doc["adept.common.HltContentContainer"]["eventMentions"]
    if (events[0] == "") :
        continue
    
    # Extract all event_mentions, coreference and entityMentions from document    
    EventMentions = events[0]["adept.common.EventMention"]
    Coreferences = doc["adept.common.HltContentContainer"]["coreferences"][0]
    EntityMentions = doc["adept.common.HltContentContainer"]["entityMentions"][0]
    
    if isinstance(EventMentions, dict) == True:
        allEventMentions = [EventMentions]
    else :
        allEventMentions = EventMentions
    
    # Extract elements of each event mention
    allEventElements = [extractElements(event) for event in allEventMentions]
    
    # Extract arguments of each event mention
    allEventArguments = [extractArguments(event, Coreferences, EntityMentions) for event in allEventElements]
    
    # Remove null arguments
    allEventArguments = [arg for arg in allEventArguments if arg != None ]
    
    if len(allEventArguments) > 0 :
        outFile = os.path.splitext(document)[0] + ".jsonl"        
        
        output = open("gdis_eventMentions\\" + outFile,"w")
        #for event in allEventArguments :
        #    output.write(json.dumps(event) + "\n")
        output.writelines([json.dumps(event)+"\n" for event in allEventArguments])
        output.close()
        

    i = i+1
    
    if i % 500 == 0 :
        print i

t2 = time.time()

print "Total time = " + str(t2-t1) + " secs"

