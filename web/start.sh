#!/bin/bash
sleep 10
source /home/pi/miniforge3/bin/activate
conda activate sf
cd /home/pi/sfgame/web
python MainProgram.py