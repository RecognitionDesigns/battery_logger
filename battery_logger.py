import anki_vector
import time

with anki_vector.Robot() as robot:
    while True:
        refTime = datetime.now().strftime(("%H:%M:%S"))
        battery_state = robot.get_battery_state()
        print(refTime)
        print("Robot battery voltage: {0}".format(battery_state.battery_volts))
        print("Robot battery Level: {0}".format(battery_state.battery_level))
        
        if robot.status.is_robot_moving:
            print("Vector is in motion.")
            status = (str("Vector is in motion."))

        if robot.status.is_picked_up:
            print("Vector is picked up.")
            status = (str("Vector is picked up."))

        if robot.status.is_pathing:
            print("Vector is traversing a path.")
            status = (str("Vector is traversing a path."))

        if robot.status.is_on_charger:
            print("Vector is on the charger.")
            status = (str("Vector is on the charger."))
            
        if robot.status.is_in_calm_power_mode:
            print("Vector is in calm power mode.")
            status = (str("Vector is in calm power mode."))
            
        if robot.status.is_falling:
            print("Vector is falling.")
            status = (str("Vector is falling."))

        if robot.status.is_docking_to_marker:
            print("Vector has found a marker and is docking to it.")
            status = (str("Vector has found a marker and is docking to it."))

        if robot.status.is_cliff_detected:
            print("Vector has detected a cliff.")
            status = (str("Vector has detected a cliff."))

        if robot.status.is_charging:
            print("Vector is currently charging.")
            status = (str("Vector is currently charging."))

        if robot.status.is_carrying_block:
            print("Vector is carrying his block.")
            status = (str("Vector is carrying his block."))

        if robot.status.is_button_pressed:
            print("Vector's button was button pressed.")
            status = (str("Vector's button was button pressed."))

        if robot.status.is_being_held:
            print("Vector is being held.")
            status = (str("Vector is being held."))

        if robot.status.is_animating:
            print("Vector is animating.")
            status = (str("Vector is animating."))

        if robot.status.are_wheels_moving:
            print("Vector's wheels are moving.")
            status = (str("Vector's wheels are moving."))
            
        f= open("battery_log.txt","a+")
        f.write(str(refTime) + ", ")
        f.write(str(battery_state.battery_volts) + ", ")
        f.write(str(battery_state.battery_level) + ", ")
        f.write((status) + "\n")
        f.close()
        
        time.sleep(5)
