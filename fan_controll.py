import os
import time
import smbus
import RPi.GPIO as GPIO

# Set the I2C address of the fan controller
FAN_CONTROLLER_I2C_ADDRESS = 0x1a

# Initialize the I2C bus
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

# Function to set the fan speed
def set_fan_speed(speed):
    try:
        bus.write_byte(FAN_CONTROLLER_I2C_ADDRESS, speed)
    except IOError:
        pass  # Handle any I2C communication errors here

# Function to get the CPU temperature
def get_cpu_temperature():
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        return float(temp.replace("temp=", "").replace("'C\n", ""))
    except ValueError:
        return 0.0

# Function to adjust the fan speed based on temperature
def adjust_fan_speed():
    while True:
        cpu_temp = get_cpu_temperature()

        if cpu_temp >= 70.0:
            set_fan_speed(100)  # Set fan speed to 100% when temperature is 65°C or higher
        elif cpu_temp >= 60.0:
            set_fan_speed(50)   # Set fan speed to 55% when temperature is between 60°C and 65°C
        elif cpu_temp >= 55.0:
            set_fan_speed(25)  # Set fan speed to 10% when temperature is between 55°C and 60°C
        else:
            set_fan_speed(0)    # Turn off the fan when temperature is below 45°C

        time.sleep(30)  # Adjust the fan speed every 30 seconds

if __name__ == "__main__":
    try:
        adjust_fan_speed()
    except KeyboardInterrupt:
        set_fan_speed(0)  # Turn off the fan when the script is stopped
