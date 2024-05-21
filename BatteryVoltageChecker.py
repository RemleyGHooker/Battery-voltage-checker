## A program to get battery percent from external battery in bytes, convert the data to string, and write the data onto a file using a rasberry pi.
## By Remley
 
import spidev
import time
import subprocess

## Variables for SPI and LDR and a delay
delay = 3600
ldr_channel = 0

spi = spidev.SpiDev()
spi.open(0, 0)

##Read in AD and give to DA
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

##read battery percentage from external batteries
def read_battery_percentage():
    try:
        output = readadc(ldr_channel)
      ## convert bytes to string
        output = output.decode("utf-8")
        lines = output.split("\n")

        for line in lines:
            if "Battery Percentage:" + ((output/5)*100) in line:
                ## take out whitespace, split into 
                ## words and assign list location 
                percentage = line.strip().split()[1]
                return percentage
    ## if it dosen't work output an error message 
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)

    return None

## write battery percentage to a file
def write_battery_percentage_to_file(percentage):
    with open("battery_percentage.txt", "w") as file:
        file.write(percentage)
      ## SO that I don't overload stuff
        time.sleep(delay)

## Read battery percentage from external batteries
battery_percentage = read_battery_percentage()

## If battery percentage is valid, write to file and print sucess.
if battery_percentage is not None:
    write_battery_percentage_to_file(battery_percentage)
    print("Battery percentage written to file.")
else:
    print("Failed to read battery percentage.")