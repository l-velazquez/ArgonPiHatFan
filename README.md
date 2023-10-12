# Argon One Fan Pi Hat Python Script

I created this python script because when I ran the Argon One bash script it always made my computer reboot under load. I used the open source bashscript to generate this python script and so far it been working with no problems.


The issue I see is that the user need to make this python script run on reboot. This should not be to hard for unix expirence folks but this process can be improved in the future.

I can see the ablility of making a desktop app that can improve this expirence.

Other aspect not considered are the changing of the fan speed that are already baked in the python script and the user does not have to set them. But I understand that these setting may not fit for everyones need and should be able to easily modify if they want to do so.


To run this python script if you want to test setting

```bash
python fan_controll.py
``` 


In the function adjust fan speed you can change the fan speed
```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
s
