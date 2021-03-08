#!/bin/bash

PROJECT_HOME=$HOME/projects/tuftCam

if curl http://0.0.0.0:5000; then
    echo "server is up"; 
else
    echo "server is down";
    PYTHONPATH=$PROJECT_HOME python3 $PROJECT_HOME/api/app.py &
fi