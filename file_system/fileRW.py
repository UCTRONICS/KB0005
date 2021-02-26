import machine
import utime
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)
reading = sensor_temp.read_u16() * conversion_factor
temperature = 27 - (reading - 0.706)/0.001721
file = open("temps.txt","w")
file.write(str(temperature))
file.read()
file.close()
file = open("temps.txt")
print(file.read())
file.close()