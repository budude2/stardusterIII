from smbus2 import SMBus
import time

bus = SMBus(1)

bus.write_byte_data(0x28, 0, 0)

data = bus.read_i2c_block_data(0x28, 0, 4)

while((data[0] & 192) == 128):
    data = bus.read_i2c_block_data(0x28,0,4)

print(data)

press_raw = (data[0] << 8) + data[1]
print(press_raw)

press = (press_raw - 1638) * 15 / 13107 + 0.48
print(press, "psi")

press_mb = round(press * 68.947572931783, 2)
print(press_mb, "mb")

pressure_inhg = round(press * 2.03602, 2)
print(pressure_inhg, "inhg")
