def get_device():
    DC = 24
    RST = 25
    try:
        from luma.oled.device import sh1106
        from luma.core.interface.serial import spi
    except ImportError:
        print("Libs needed.")
    except Exception as e:
        print(e)
    serial = spi(device=0, port=0, bus_speed_hz=8000000, transfer_size=4096,gpio_DC=DC, gpio_RST=RST)
    return(sh1106(serial, rotate=2))

