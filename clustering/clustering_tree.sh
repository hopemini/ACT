#!/bin/bash

mkdir result
mkdir visualization

export PYTHONPATH=.

echo 'Start Clustering'
ITERATION=( "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" )
CLASSNUM=( "23" "34" )

for n in ${CLASSNUM[@]}; do
    for i in ${ITERATION[@]}; do
        echo "tree_${n}_${i} clustering start"
        python clustering.py -d tree_${n}_${i} -k ${CLASSNUM}
    done
done

echo 'Done...'
