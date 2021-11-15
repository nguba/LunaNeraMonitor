from unittest import TestCase

from PXU import PXU


class TestPXU(TestCase):

    def test_pxu_startup(self):
        pxu = PXU('COM4', device_id=5)
        pxu.close()

    def test_read_process_value(self):
        try:
            pxu = PXU('COM4', device_id=5)
            pv = pxu.read_pv()
            print(pv)
            self.assertIsNotNone(pv)
        finally:
            pxu.close()

