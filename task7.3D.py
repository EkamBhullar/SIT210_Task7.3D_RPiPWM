#SIT 210 Task 7.3D
#By-Ekamjot Singh,2210994782

from time import sleep
from gpiozero import DistanceSensor, PWMLED

# Create a PWM LED on GPIO pin 17
led = PWMLED(17)

# Create a distance sensor with echo on GPIO pin 23 and trigger on GPIO pin 24
distance_sensor = DistanceSensor(echo=23, trigger=24)

# Main function to control the LED brightness based on distance
def main():
    # Turn on the LED initially
    led.on()

    while True:
        # Get the distance from the sensor
        distance = distance_sensor.value
        print(f'Distance: {distance:1.2f} meters')

        # Calculate the duty cycle for LED brightness
        brightness = round(1.0 - distance, 1)

        # Ensure the brightness is not below 0
        if brightness < 0:
            brightness = 0.0

        # Set the LED brightness
        led.value = brightness

        # Sleep for a short duration
        sleep(0.1)

    # Clean up and close the sensor (not reached in this example)

# Call the main function directly
main()
