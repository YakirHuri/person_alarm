#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <number1> <number2>"
    exit 1
fi

# Get the float number from the first argument
START_ANGLE=$1
END_ANGLE=$2
PIN_NUM=$3



# Pass the float number to the Python script
sudo python3 /home/liran/person_alarm/motor/motor.py "$START_ANGLE" "$END_ANGLE" "$PIN_NUM"
