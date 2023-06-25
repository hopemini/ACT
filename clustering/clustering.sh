#!/bin/bash

mkdir result
mkdir visualization

export PYTHONPATH=.

echo 'Start Clustering'
TYPES=( "add" "cat" )
WEIGHTS=( "0.1" "0.2" "0.3" "0.4" "0.5" "0.6" "0.7" "0.8" "0.9" )
ITERATION=( "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" )
CLASSNUM=( "23" "34" )
CONVTYPES=( "re" )

for n in ${CLASSNUM[@]}; do
    echo "rico_${n} clustering start"
    python clustering.py -d rico_${n} -k ${n}
    for i in ${ITERATION[@]}; do
        echo "tree_${n}_${i} clustering start"
        python clustering.py -d tree_${n}_${i} -k ${n}
        for CONVTYPE in ${CONVTYPES[@]}; do
            echo "conv_${CONVTYPE}_${n}_${i} clustering start"
            python clustering.py -d conv_${CONVTYPE}_${n}_${i} -k ${n}
        done
        for TYPE in ${TYPES[@]}; do
            echo "rico_tree_${n}_${i}_${TYPE} clustering start"
            python clustering.py -d rico_${n}_tree_${n}_${i} -t ${TYPE} -k ${n}
        done
        for CONVTYPE in ${CONVTYPES[@]}; do
            for TYPE in ${TYPES[@]}; do
                echo "rico_conv_${CONVTYPE}_${n}_${i}_${TYPE} clustering start"
                python clustering.py -d rico_${n}_conv_${CONVTYPE}_${n}_${i} -t ${TYPE} -k ${n}
            done
            for TYPE in ${TYPES[@]}; do
                echo "tree_conv_${CONVTYPE}_${n}_${i}_${TYPE} clustering start"
                python clustering.py -d tree_${n}_${i}_conv_${CONVTYPE}_${n}_${i} -t ${TYPE} -k ${n}
            done
        done
        for TYPE in ${TYPES[@]}; do
            for WEIGHT in ${WEIGHTS[@]}; do
                echo "rico_tree_${n}_${i}_${TYPE}_${WEIGHT} clustering start"
                python clustering.py -d rico_${n}_tree_${n}_${i} -t ${TYPE} -w ${WEIGHT} -k ${n}
            done
        done
        for CONVTYPE in ${CONVTYPES[@]}; do
            for TYPE in ${TYPES[@]}; do
                for WEIGHT in ${WEIGHTS[@]}; do
                    echo "rico_conv_${CONVTYPE}_${n}_${i}_${TYPE}_${WEIGHT} clustering start"
                    python clustering.py -d rico_${n}_conv_${CONVTYPE}_${n}_${i} -t ${TYPE} -w ${WEIGHT} -k ${n}
                done
            done
            for TYPE in ${TYPES[@]}; do
                for WEIGHT in ${WEIGHTS[@]}; do
                    echo "tree_conv_${CONVTYPE}_${n}_${i}_${TYPE}_${WEIGHT} clustering start"
                    python clustering.py -d tree_${n}_${i}_conv_${CONVTYPE}_${n}_${i} -t ${TYPE} -w ${WEIGHT} -k ${n}
                done
            done
        done
    done
done

echo 'Done...'
