#!/usr/bin/python3

from smbus import SMBus

I2C_ADDR = 0x78

class HSC:
    def __init__(self, busno):
        self.bus = SMBus(1)

    # This function returns the pressure in PSI
    def read_pressure(self):

        # Trigger the pressure sensor to read data
        self.bus.write_byte(I2C_ADDR, 0)

        # Read the response
        data = self.bus.read_i2c_block_data(I2C_ADDR, 0, 4)

        # If the data isn't valid keep polling until it is.
        while((data[0] & 0xC0) == 0x80):
            data = self.bus.read_i2c_block_data(I2C_ADDR, 0, 4)

        # Combine data bytes
        press_raw = (data[0] << 8) + data[1]

        # Return the pressure in PSI
        return round(((press_raw - 1638) * 1600 ) / 13107 + 23, 2)
