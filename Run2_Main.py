from spike import MotorPair,Motor
from spike.control import wait_for_seconds
#truck mission
movement_motors = MotorPair('A','B') # Set up the movement motors (wheels)
right_motor = Motor('B')
left_motor = Motor('A')
extension_motor= Motor ('D')

movement_motors.set_default_speed(60) # Set up the motor speed

movement_motors.move(45,'cm') # moving the robot forwards

right_motor.run_for_degrees(600)# turning to mission
#extension_motor.set_default_speed(100)

extension_motor.run_for_degrees(-40,80)#taking energy cubes
extension_motor.run_for_degrees(40,80)
extension_motor.run_for_degrees(-40,80)
extension_motor.run_for_degrees(40,80)
extension_motor.run_for_degrees(-40,80)
#start of solar mission
movement_motors.move(-8,'cm')# moves back
#extension_motor.run_for_degrees(-50)#Turning to solar mission
right_motor.run_for_degrees(-590)
#left_motor.run_for_degrees(80,'cm')
movement_motors.move(25,'cm')
#left_motor.run_for_degrees(-100)
extension_motor.run_for_degrees(40,100)#the wheels for the robot moves 40 degrees at 100 speed
movement_motors.move(18,'cm')#robot moves 18 centimieters forward 
movement_motors.move(-15,'cm')#robot moves 15 centimieters backwards
left_motor.run_for_degrees(-250)
movement_motors.move(23,'cm')
movement_motors.move(-34,'cm')
right_motor.run_for_degrees(-850)
movement_motors.move(10,'cm')
right_motor.run_for_degrees(-400)
movement_motors.move(52,'cm')
