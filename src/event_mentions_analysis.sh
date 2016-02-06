#!/bin/bash

cwd=/home/gaurav_sathe/Lorelie/gdis/*

eventsGlobal=[]

i=1

t1="$(date +%s)"

for file_record in $cwd
do
	# Extract first event
	firstEvent=$(./jq-linux64 ".[\"adept.common.HltContentContainer\"]|.[\"eventMentions\"]|.[0]" $file_record)
	
	# Check type of first event mention
	firstEventType=$(echo $firstEvent | ./jq-linux64 "type")
	
	# Check if record has atleast one event mention from the type
	if [ $firstEventType == "\"object\"" ]
	then
	
		allMentions=$(echo $firstEvent | ./jq-linux64 ".[\"adept.common.EventMention\"]")
		
		if [ $(echo $allMentions | ./jq-linux64 "type") == "\"object\"" ]
		then
			allMentions="[$allMentions]"
		fi
		
		allMentionsTrunc=$(echo $allMentions | ./jq-linux64 "map(.[\"arguments\"]|.[0]|.[\"elements\"]|.[0] | if . != "\"\"" then . else empty end)")
		
		allMentionsArgs=$(echo $allMentionsTrunc | ./jq-linux64 'map(.["adept.common.EventMentionArgument"]|if type == "object" then [{"eventType":.["eventType"],"role":.["role"]}] elif type == "array" then map({"eventType":.["eventType"],"role":.["role"]}) else empty end | {"adept.common.EventMentionArgument":.})')
		
		#eventsGlobal=$(echo "{\"allEvents\":$eventsGlobal, \"currEvents\":$allMentionsArgs}" | ./jq-linux64 '.["allEvents"] + .["currEvents"]')
		
		echo $allMentionsArgs > "/home/gaurav_sathe/Lorelie/gdis_eventMentions/$(basename $file_record '.json')_trunc.json"
		
		
	fi
	
	i=$((i+1))
	
	if ! ((i % 500)); then echo $i; fi
done

t2="$(date +%s)"
#echo $eventsGlobal > "allEventMentions.json"

echo "Total time = $((t2-t1)) secs"
