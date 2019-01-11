
import tello
import time

drone = tello.Tello()
drone.send_command_init()
drone.takeoff()
drone.move_up(40)
drone.move_down(40)
drone.land()

print 'Flight time: %s' % drone.get_flight_time()
