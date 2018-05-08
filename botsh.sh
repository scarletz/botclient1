#!/bin/sh

python mainstream.py
6_createVisData.sh ../ ../app
7_visualization.sh ../app
python delete.py

