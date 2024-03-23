#!/usr/bin/env python3
# Python script to retrieve and parse a DSMR telegram from a P1 port
import asyncio
import datetime
import re
import storage
import sys
import serial

from constants import list_of_codes

max_len = max(map(len, list_of_codes.values()))

# Program variables
# The true telegram ends with an exclamation mark after a CR/LF
pattern = re.compile('\r\n(?=!)')
# Create an empty telegram
telegram = ''
checksum_found = False

# Serial port configuration
ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.SEVENBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 12
ser.port = "/dev/serial0"


async def retrieve(app) -> dict:
    while True:
        try:
            # Read in all the lines until we find the checksum (line starting with an exclamation mark)
            # Open serial port
            ser.open()
            telegram = ''
            checksum_found = False

            while not checksum_found:
                # Read in a line
                telegram_line = ser.readline()
                # Check if it matches the checksum line (! at start)
                if re.match(b'(?=!)', telegram_line):
                    telegram = telegram + telegram_line.decode()
                    checksum_found = True
                else:
                    telegram = telegram + telegram_line.decode()

        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            print(f"There was a problem {ex}, continuing...")
        # Close serial port
        try:
            ser.close()
        except:
            sys.exit("Oops %s. Programma afgebroken." % ser.name)

        # We have a complete telegram, now we can process it.
        # Store the values in a dictionary
        telegram_values = dict()
        # Split the telegram into lines and iterate over them
        for telegram_line in telegram.split('\r\n'):
            # Split the OBIS code from the value
            # The lines with a OBIS code start with a number
            if re.match('\d', telegram_line):
                # The values are enclosed with parenthesis
                # Find the location of the first opening parenthesis,
                # and store all split lines
                code = ''.join(re.split('(\()', telegram_line)[:1])
                value = ''.join(re.split('(\()', telegram_line)[1:])
                # Cleanup value
                # Gas needs another way to cleanup
                if code in list_of_codes:
                    if 'm3' in value:
                        (time, value) = re.findall('\((.*?)\)', value)
                        value = float(value.lstrip('\(').rstrip('\)*m3'))
                    else:
                        value = float(value.lstrip('\(').rstrip('\)*kWhA'))

                    telegram_values[code[4:]] = {
                        "value": value,
                        "description": list_of_codes[code]
                    }

        telegram_values["timestamp"] = {
            "value": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": "Timestamp of measurement as 'YYYY-MM-DD HH:MM:SS'"
        }
        print("P1 Reader successfully read telegram...")
        app["p1telegram"] = telegram_values
        if app["pg_pool"]:
            await storage.write(telegram_values, app["pg_pool"])
        await asyncio.sleep(9)
