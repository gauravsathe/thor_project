#!/bin/bash

noOfMentions=$(./jq-linux64 '.|length' allEventMentions.json)

echo "Total Mentions = $noOfMentions"
i=0

allMentions=""

while [ $i -lt $noOfMentions ]
do
	event=$(./jq-linux64 ".[$i]" allEventMentions.json)
	
	#index=$(curl -s -XPOST "http://localhost:9200/all_event_mentions/event/" -d "$event" > errorLog)
	
	#echo "{\"index\": {\"_index\":\"test\",\"_type\":\"test_events\",\"_id\":\"$i\"}}" >> esIndex
	
	#echo "$event" >> esIndex             
	
	allMentions="$allMentions{\"index\": {\"_index\":\"test\",\"_type\":\"test_events\",\"_id\":\"$i\"}}$event"
	
	i=$((i+1))
	
	if ! ((i % 500))
	then 
		echo $i
		printf "%s" $allMentions >> esIndex
		allMentions=""
	fi
done


