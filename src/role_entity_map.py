# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:57:50 2016

@author: gaurav_sathe
"""

# A mapping from : "roles" of entities in eventMention --> ontology schema
role_entity_map =   {
                        # Temporal entities                        
                        "Time-Within" : "date-time",                        
                        
                        # Location based entities
                        "Place" : "location",
                        "Destination" : "location",                        
                        "Position" : "location",
                        "Origin" : "location",                        
                        
                        # Entities affected by the event
                        "Victim" : "affected",
                        "Target" : "affected",
                        "Entity" : "affected",
                        "Defendant" : "affected",
                        "Recipient" : "affected",                        
                        "Beneficiary" : "affected",                        
                        
                        # Entities who caused the event
                        "Instrument" : "caused",                        
                        "Attacker" : "caused",
                        "Giver" : "caused",
                        "Plaintiff" : "caused",
                        "Buyer" : "caused",
                        "Adjudicator" : "caused",
                        "Prosecutor" : "caused",
                        "Seller" : "caused",
                        
                        # Action type entities
                        "Crime" : "consequence",
                        "Sentence" : "consequence",                        
                        
                        # Persons or organizations involved in the event
                        "Agent" : "observed",             # Depends on event
                        "Person" : "observed",                        
                        "Org" : "observed",
                        
                        "Vehicle" : "object",                        
                        "Price" : "object",
                        "Artifact" : "object",
                        "Money" : "object"
                    }