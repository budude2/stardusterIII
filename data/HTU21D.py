import pigpio

I2C_ADDR           = 0x40
CMD_TRIG_TEMP_HM   = 0xE3
CMD_TRIG_HUMID_HM  = 0xE5
CMD_TRIG_TEMP_NHM  = 0xF3
CMD_TRIG_HUMID_NHM = 0xF5
CMD_WRITE_USER_REG = 0xE6
CMD_READ_USER_REG  = 0xE7
CMD_RESET          = 0xFE
    
class HTU21D:
    def __init__(self, busno):
        self.bus = pigpio.pi()
        self.handle = self.bus.i2c_open(busno, I2C_ADDR, 0)

    def read_temperature(self):
        self.reset()
        (stat, data) = self.bus.i2c_read_i2c_block_data(self.handle, CMD_TRIG_TEMP_HM, 3)
        self.bus.i2c_close(self.handle)
        return -46.85 + 175.72 * (data[1] * 256 + data[0]) / 65536
     
    def read_humidity(self):
        self.reset()
        (stat, data) = self.bus.i2c_read_i2c_block_data(self.handle, CMD_TRIG_HUMID_HM, 3)
        return -6 + 125 * (data[0] * 256 + data[1]) / 65536.0

    def reset(self):
        self.bus.i2c_write_byte(self.handle, CMD_RESET)

if __name__ == '__main__':
   htu = HTU21D(1)
   #print(htu.read_temperature())
   print(htu.read_humidity())
