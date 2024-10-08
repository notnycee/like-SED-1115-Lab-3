from machine import Pin
import time

# Set up the LED and button
led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Initial state for the LED and button
led1_state = False
led1.value(0) # making sure the value of the LED is nothing because its off
sw5_prev_state = False #button is off

while True:
    # Read the current state of the button
    sw5_current_state = sw5.value()
   
    # If button is pressed a value which is different from the previous state is read and the state of the button is no longer false(previous state)
    if sw5_current_state and not sw5_prev_state:
        led1_state = not led1_state  # Flips the current state of the LED, LED which was originally off will turn on.
        led1.value(led1_state)  # LED value will actually change to the LED value of the new state

    # Now the current state of the button become the previous state
    sw5_prev_state = sw5_current_state

    # delay to debounce the button
    time.sleep(0.01)
# loop will go on forever