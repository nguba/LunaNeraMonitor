import logging


class Logger:

    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S%p', level=logging.DEBUG)

    def pxu_start(self, device_id: int) -> None:
        logging.info(" Connecting to PXU Controller id=%s", device_id)

    def pxu_stop(self, device_id):
        logging.info(" Disconnected from PXU Controller id=%s", device_id)
