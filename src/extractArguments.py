# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:56:29 2016

@author: gaurav_sathe
"""

from role_entity_map import role_entity_map
from os.path import basename

def extractArguments(event, Coreferences, EntityMentions) :
    
    try :
        allArguments = event["elements"]["adept.common.EventMentionArgument"]
    except Exception as e:
        return None
    
    if isinstance(allArguments, dict) :
        allArguments = [allArguments]
    
    docId = Coreferences["adept.common.Coreference"][0]["entities"][0]["adept.common.Entity"]["canonicalMention"]["docId"]
    
    eventArgs = {"docId":docId, "eventType":event["eventType"]}
    
    for arg in allArguments :
        role = arg["role"]["type"]        
        try : 
            ref = arg["filler"]["@reference"] 
            
            entityRef = processReference(ref, Coreferences, EntityMentions)            
        except Exception as e :
            entityRef = {"value" : arg["filler"]["value"]}
        
        ontRef = role_entity_map[role]
        if ontRef in eventArgs.keys() :
            eventArgs[ontRef].append(entityRef)
        else :
            eventArgs[ontRef] = [entityRef]
    
    for key in eventArgs.keys() :
        args = eventArgs[key]        
        if isinstance(args, list) and len(args) == 1 :
            eventArgs[key] = args[0]
    
    
    
    return eventArgs
    
def processReference(ref, Coreferences, EntityMentions) :
    
    refKeys = ref.split("/")
    
    refKeys = refKeys[6:]
    
    if refKeys[0] == "coreferences" :
        key = refKeys[1]
        
        pos = key.find("[")
        
        if pos == -1 :
            index = 0
        else :
            index = int(key[pos+1:-1]) - 1
        
        coref = Coreferences["adept.common.Coreference"][index]
        
        if refKeys[2] == "entities" :
            entityValue = coref[refKeys[2]][0][refKeys[3]][refKeys[4]]["value"]
            entityType = coref[refKeys[2]][0][refKeys[3]][refKeys[4]]["entityType"]["type"]
            entityContext = coref[refKeys[2]][0][refKeys[3]][refKeys[4]]["context"]["value"]
        
        else :
            key = refKeys[3]
        
            pos = key.find("[")
            
            if pos == -1 :
                index = 0
            else :
                index = int(key[pos+1:-1]) - 1            
            
            try :
                entityValue = coref[refKeys[2]][0]["adept.common.EntityMention"][index]["value"]
                entityType = coref[refKeys[2]][0]["adept.common.EntityMention"][index]["entityType"]["type"]
                entityContext = coref[refKeys[2]][0]["adept.common.EntityMention"][index]["context"]["value"]
            
            except KeyError :
                entityValue = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["value"]
                entityType = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["entityType"]["type"]
                entityContext = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["context"]["value"]
    
    else :
        key = refKeys[1]
        
        pos = key.find("[")
        
        if pos == -1 :
            index = 0
        else :
            index = int(key[pos+1:-1]) - 1
        
        entity = EntityMentions["adept.common.EntityMention"][index]
        
        try :
            entityValue = entity["value"]
            entityType = entity["entityType"]["type"]
            entityContext = entity["context"]["value"]
            
        except KeyError :
            ref = entity["@reference"]
            
            refKeys = ref.split("/")
            
            refKeys = refKeys[2:]
            
            key = refKeys[1]
        
            pos = key.find("[")
            
            if pos == -1 :
                index = 0
            else :
                index = int(key[pos+1:-1]) - 1
            
            coref = Coreferences["adept.common.Coreference"][index]
            
            entityValue = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["value"]
            entityType = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["entityType"]["type"]
            entityContext = coref["entities"][0]["adept.common.Entity"]["canonicalMention"]["context"]["value"]
    
    entityRef = {"value" : entityValue, "type" : entityType, "context" : entityContext}
    
    return entityRef
            
            
            
            
            
            
            