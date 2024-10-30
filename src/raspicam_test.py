

#python3 -m venv myenv


#source myenv/bin/activate


#pip3 install picamera
#export READTHEDOCS=True

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
