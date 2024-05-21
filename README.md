# Battery-voltage-checker
A program to get battery percent from external battery in bytes, convert the data to string, and write the data onto a file using a raspberry pi.
# Battery Percentage Reader

This project reads the battery percentage from an external battery using a Raspberry Pi, converts the data from bytes to a string, and writes the data to a file. The project utilizes the SPI protocol to communicate with the battery, making use of the `spidev` library.

## Features
- Reads battery percentage from an external battery.
- Converts the data from bytes to a readable string.
- Writes the battery percentage to a file.
- Includes error handling for subprocess calls.
- Delays the reading process to prevent overloading.

## Requirements
- Raspberry Pi
- External battery with SPI communication capability
- MCP3008 ADC (Analog-to-Digital Converter)
- Python 3.x
- `spidev` library

## Installation

1. Install the `spidev` library if you haven't already:
    ```sh
    sudo apt-get update
    sudo apt-get install python3-spidev
    ```

2. Clone this repository:
    ```sh
    git clone https://github.com/RemleyGHooker/battery-percentage-reader.git
    cd battery-percentage-reader
    ```

## Usage

1. Ensure your Raspberry Pi is connected to the external battery via SPI.
2. Run the script:
    ```sh
    python3 battery_percentage_reader.py
    ```

## Code Explanation

## readadc(adcnum): 
Reads data from the specified ADC channel.
## read_battery_percentage(): 
Reads and converts the battery percentage from the ADC output.
## write_battery_percentage_to_file(percentage):
Writes the battery percentage to a file and waits for the specified delay.


### Import Libraries
```python
import spidev
import time
import subprocess
