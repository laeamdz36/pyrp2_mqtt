"""Module to read data from sensor RP"""
import datetime as dt
import bme280
import smbus2
from gpiozero import CPUTemperature
from gpiozero.pins.native import NativeFactory
from gpiozero import Device

Device.pin_factory = NativeFactory()


def get_cpu_temp():
    """Reading temperature from CPU"""
    cpu = None
    try:
        cpu = CPUTemperature()
        print(f"Current temperature: {cpu.temperature}")
        cpu = round(float(cpu.temperature), 2)
    except Exception as e:
        print(f"Error: {e.args}")
    return cpu


def read_sensor():
    """Read sensor BME 280 in  76"""
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)
    bme280_data = bme280.sample(bus, address)
    # data asignation
    temperature = round(float(bme280_data.temperature), 2)
    humidity = round(float(bme280_data.humidity), 2)
    pressure = round(float(bme280_data.pressure), 2)
    # logging
    t_stamp_lg = f"Tiempo: {bme280_data.timestamp}"
    hum_lg = f"Humedad actual: {humidity} %"
    press_lg = f"Presion actual: {pressure} hPa"
    temp_lg = f"Temperatura: {temperature} °C"
    now = dt.datetime.today()
    head = now.strftime("%d/%m/%Y %H%M%S")
    print(head.center(50, "="))
    print(t_stamp_lg, hum_lg, press_lg, temp_lg, sep="\n")

    return {"humidity": humidity, "pressure": pressure,
            "temperature": temperature, }


if __name__ == "__main__":
    _data = read_sensor()
