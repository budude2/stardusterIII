from smbus import SMBus

I2C_ADDR = 0x28

class HSC:
    def __init__(self, busno):
        self.bus = SMBus(busno)

    # This function returns the pressure in PSI
    def read_pressure(self):

        # Trigger the pressure sensor to read data
        self.bus.write_byte(0x28, 0)

        # Read the response
        data = self.bus.read_i2c_block_data(0x28, 4)

        # If the data isn't valid keep polling until it is.
        while((data[0] & 0xC0) == 0x80):
            data = self.bus.read_i2c_block_data(0x28, 4)

        # Combine data bytes
        press_raw = (data[0] << 8) + data[1]

        # Return the pressure in PSI
        return (press_raw - 1638) * 15 / 13107 + 0.46

    def read_pressure_mb(self):
        psi = self.read_pressure()

        return round(psi * 68.947572931783, 2)
