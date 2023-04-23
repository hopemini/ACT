#!/bin/bash

export PYTHONPATH=.
python evaluation_tree.py -e purity
python evaluation_tree.py -e nmi
python evaluation_tree.py -e ari
echo 'Done...'
