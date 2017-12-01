import pigpio

I2C_ADDR = 0x78

class HSC:
    def __init__(self, busno):
        self.bus = pigpio.pi()
        self.handle = self.bus.i2c_open(busno, I2C_ADDR, 0)

    # This function returns the pressure in PSI
    def read_pressure(self):

        # Trigger the pressure sensor to read data
        self.bus.i2c_write_byte(self.handle, 0)

        # Read the response
        (stat, data) = self.bus.i2c_read_i2c_block_data(self.handle, 0, 4)

        # If the data isn't valid keep polling until it is.
        while((data[0] & 0xC0) == 0x80):
            (stat, data) = self.bus.i2c_read_i2c_block_data(self.handle, 0, 4)

        # Combine data bytes
        press_raw = (data[0] << 8) + data[1]

        self.bus.i2c_close(self.handle)

        # Return the pressure in PSI
        return round(((press_raw - 1638) * 1600 ) / 13107 + 23, 2)
