from machine import Pin, I2C
from time import sleep
import neopixel

i2c = I2C(1,scl=Pin(22),sda=Pin(21))
address = 0x68
i2c.writeto(address,bytearray([0x1A,0x00]))
i2c.writeto(address,bytearray([0x1B,0x00]))
i2c.writeto(address,bytearray([0x1C,0x00]))

try:
    counter = 0
    while True:

      Accel = bytearray(6)
      i2c.writeto(address,bytearray([0x3B]))
      Accel = i2c.readfrom(address,6)
      
      Accel_X = bytearray(2)
      Accel_X = Accel[0]*256+Accel[1]
      Accel_Y = bytearray(2)
      Accel_Y = Accel[2]*256+Accel[3]
      Accel_Z = bytearray(2)
      Accel_Z = Accel[4]*256+Accel[5]
      
      if int.from_bytes(Accel_X,"little") > 32767:
        Accel_X = int.from_bytes(Accel_X,"little") - 65536
      else:
        Accel_X = int.from_bytes(Accel_X,"little")

      if int.from_bytes(Accel_Y,"little") > 32767:
        Accel_Y = int.from_bytes(Accel_Y,"little") - 65536
      else:
        Accel_Y = int.from_bytes(Accel_Y,"little")

      if int.from_bytes(Accel_Z,"little") > 32767:
        Accel_Z = int.from_bytes(Accel_Z,"little") - 65536
      else:
        Accel_Z = int.from_bytes(Accel_Z,"little")

      print("%4.2f, %4.2f, %4.2f " % ((Accel_X)/16384,(Accel_Y)/16384,(Accel_Z)/16384))
      
      #time.sleep(1)
      counter += 1

except:
    print('An error occured')