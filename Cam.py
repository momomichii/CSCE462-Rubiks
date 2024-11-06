from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

for i in range(9): #change this number for how many pictures we need

    camera.start_preview() #if we do the LED screen we would use the preview to present on LED
    sleep(2)
    camera.capture('/home/pi/Desktop/image.jpg')  #change this for the pi folder
    camera.stop_preview()

# Close the camera
camera.close()
