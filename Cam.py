from picamera import PiCamera
from time import sleep

def take_pic(i):
    # Initialize the camera
    camera = PiCamera()
    camera.start_preview() #if we do the LED screen we would use the preview to present on LED
    sleep(2)
    camera.capture(f'/home/pi/Desktop/Cube_Pic/image{i}.jpg')
    camera.stop_preview()
    # Close the camera
    camera.close()
    
def main():
    i = 0 
    while(i < 1):
        take_pic(i)
        i+=1
        #move the position of the cube (change the steps)
        take_pic(i)
        i+=1
        #repeat this until this is done
    

    


