from machine import Pin, I2C
from time import sleep
import neopixel

i2c = I2C(1,scl=Pin(22),sda=Pin(21))
MPU6050_ADDR = 0x68
MPU6050_ACCEL_CONFIG = 0x1C
PWR_MGMT_1 = 0x6B

i2c.writeto(MPU6050_ADDR,bytearray([MPU6050_ACCEL_CONFIG,0x00]))
i2c.writeto(MPU6050_ADDR,bytearray([PWR_MGMT_1,0x00]))

#counter = 0
while True:
    Accel_X = bytearray(2)
    i2c.writeto(MPU6050_ADDR,bytearray([0x3B]))
    Accel_X = i2c.readfrom(MPU6050_ADDR,2)    
    if int.from_bytes(Accel_X,"big") > 32767:
        Accel_X = int.from_bytes(Accel_X,"big") - 65536
    else:
        Accel_X = int.from_bytes(Accel_X,"big")
    
    Accel_Y = bytearray(2)
    i2c.writeto(MPU6050_ADDR,bytearray([0x3D]))
    Accel_Y = i2c.readfrom(MPU6050_ADDR,2)    
    if int.from_bytes(Accel_Y,"big") > 32767:
        Accel_Y = int.from_bytes(Accel_Y,"big") - 65536
    else:
        Accel_Y = int.from_bytes(Accel_Y,"big")
    
    Accel_Z = bytearray(2)
    i2c.writeto(MPU6050_ADDR,bytearray([0x3F]))
    Accel_Z = i2c.readfrom(MPU6050_ADDR,2)    
    if int.from_bytes(Accel_Z,"big") > 32767:
        Accel_Z = int.from_bytes(Accel_Z,"big") - 65536
    else:
        Accel_Z = int.from_bytes(Accel_Z,"big")
    
    print("x: %4.2f, y: %4.2f, z: %4.2f" % ((Accel_X)/16384,(Accel_Y)/16384,(Accel_Z)/16384))
  
    #time.sleep(1)
    #counter += 1