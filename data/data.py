import max31865
import HSC
import HTU21D

pres = HSC.HSC(1)
hum = HTU21D.HTU21D(1)

print("Pressure (mb): " + str(pres.read_pressure_mb()))
print("Humidity (rh): " + str(round(hum.read_humidity(), 2)))
print("Temp (c): " + str(round(hum.read_temperature(), 2)))
