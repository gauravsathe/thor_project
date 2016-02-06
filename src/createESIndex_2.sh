#!/bin/bash

cwd="/home/gaurav_sathe/Lorelie/gdis_eventMentions_2/*"
i=0

allMentions=""

for file_record in $cwd
do
	noOfEvents=$(./jq-linux64 '.|length' $file_record)

	j=0
	while [ $j -lt $noOfEvents ]; do
		event='{"index": {"_index":"allMentions","_type":"event","_id":"$i"}}$(./jq-linux64 ".[$j]" $file_record)'

		printf "%s" $event >> esIndex_2
		
		j=$((j+1))	
	done
	
	i=$((i+1))

	if ! ((i % 500)); then
		echo $i
	fi
done
