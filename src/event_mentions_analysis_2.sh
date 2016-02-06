#!/bin/bash

cwd=/home/gaurav_sathe/Lorelie/gdis/*

#eventsGlobal=[]

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
		
		allMentionsTrunc=$(echo $allMentions | ./jq-linux64 'map(if (.["arguments"]|.[0]|.["elements"]|.[0]) != "" then {"eventType":.["eventType"]|.["type"],"arguments":(.["arguments"]|.[0]|.["elements"]|.[0])} else empty end)')
		
		allMentionsArgs=$(echo $allMentionsTrunc | ./jq-linux64 'map(if (.["arguments"]|.["adept.common.EventMentionArgument"]|type) == "object" then {"eventType":.["eventType"],"eventArguments":{"role":.["arguments"]|.["adept.common.EventMentionArgument"]|.["role"]|.["type"]}} elif (.["arguments"]|.["adept.common.EventMentionArgument"]|type) == "array" then {"eventType":.["eventType"],"eventArguments":.["arguments"]|.["adept.common.EventMentionArgument"]|map({"role":.["role"]|.["type"]})} else empty end)')
		
		#eventsGlobal=$(echo "[$eventsGlobal, $allMentionsArgs]" | ./jq-linux64 'add')
		#eventsGlobal=$(echo $eventsGlobal | ./jq-linux64 "[.[] , $allMentionsArgs]")
		echo $allMentionsArgs > "/home/gaurav_sathe/Lorelie/gdis_eventMentions_2/$(basename $file_record '.json')_trunc.json"
	fi
	
	i=$((i+1))
	
	if ! ((i % 500)); then echo $i; fi
done

t2="$(date +%s)"

#eventsGlobal=$(echo $eventsGlobal | ./jq-linux64 'add')

#echo $eventsGlobal > "allEventMentions_2.json"

echo "Total time = $((t2-t1)) secs"
