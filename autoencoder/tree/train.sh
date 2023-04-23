#!/bin/bash

mkdir log
mkdir log/check_point
mkdir log/plot
mkdir log/pth

export PYTHONPATH=.
echo 'Start tree autuencoder training...'
python main/train.py -i 10

echo 'vector save...'
python main/vector_save.py -i 10

echo 'done...'
