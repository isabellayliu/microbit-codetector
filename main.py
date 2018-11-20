import microbit

seconds = 0

DELAY = 1000
SENSOR = microbit.pin0
CURRENT_READING = None

def main():
    """
    Main program loop
    """
    global seconds
    while True:
        reading = SENSOR.read_analog()
        microbit.display.show(str(reading))
        print((seconds, reading))
        seconds = seconds + (DELAY // 1000)
        # Sleep until  next measurement
        microbit.sleep(DELAY)
    

if __name__ == '__main__':
    # Run the program loop.
    main()