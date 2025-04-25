"""Module to read data from sensor RP"""
import bme280
import smbus2


def read_sensor():
    """Read sensor BME 280 in  76"""
    port = 1
    address = 0x76  # Adafruit BME280 address. Other BME280s may be different
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


def _log_data(data):
    """Log data in console"""

    for meas, value in data.items():
        print(meas, value, flush=True)


if __name__ == "__main__":
    _data = read_sensor()
    _log_data(_data)
