# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:33:55 2016

@author: gaura
"""

def extractElements(event) :
    try :
        elements = event["arguments"][0]["elements"]
    except KeyError as e :
        return None

    if elements[0] == "" :
        return None
    
    allElements = {"eventType" : event["eventType"]["type"], "elements":elements[0]}
    
    return allElements