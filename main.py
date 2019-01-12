
import tello
import time

drone = tello.Tello()
drone.send_command_init()
drone.takeoff()
drone.move_up(80)
#drone.rotate_cw(90)
drone.rotate_ccw(90)
drone.move_forward(130)
drone.rotate_ccw(90)
drone.move_forward(180)
drone.rotate_ccw(90)
drone.move_forward(50)
drone.get_battery()
drone.land()

print 'Flight time: %s',drone.get_flight_time()
