#!/bin/bash

docker run --rm -it \
	--name person_alarm \
	-v /home/liran/person_alarm/docker_tf_lite/:/home/liran/person_alarm/docker_tf_lite/ \
	--workdir=/home/liran/person_alarm/docker_tf_lite/ \
	--network=host --privileged \
	--env DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix -v ${HOME}:/home/user cognimbus/tflite-object-detection python3 person_alarm.py
	#--env DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix -v ${HOME}:/home/user person_alrarm:latest python3 person_alarm.py

#

