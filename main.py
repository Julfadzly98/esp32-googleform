import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

ow_bus = OneWireBus(board.D2)
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
ds18.temperature
