#!/bin/sh

python mainstream.py
6_createVisData.sh ../ ../app
python dockers.py
7_visualization.sh ../app
python delete.py

