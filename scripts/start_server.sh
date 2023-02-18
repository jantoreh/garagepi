#!/bin/bash

if curl http://0.0.0.0:5000; then
    echo "server is up"; 
else
    echo "server is down";
    python3 $HOME/garagepi/app.py &
fi