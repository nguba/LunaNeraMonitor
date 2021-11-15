import server_log
import minimalmodbus


class PXU:
    def __init__(self, port, device_id):
        self.device_id = device_id
        self.log = server_log.Logger()
        self.log.pxu_start(self.device_id)
        self.instrument = minimalmodbus.Instrument(port, self.device_id, debug=False)
        self.instrument.serial.baudrate = 19200
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 0.05
        self.instrument.mode = minimalmodbus.MODE_RTU

    def close(self):
        self.instrument.serial.close()
        self.log.pxu_stop(self.device_id)

