sudo docker run --rm -it \
	--name person_alarm \
	-v /home/liran/person_alarm_ws:/home/liran/person_alarm_ws \
	--workdir=/home/liran/person_alarm_ws \
	--network=host --privileged \
	--env DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix -v ${HOME}:/home/user person_alrarm:latest bash
