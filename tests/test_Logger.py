import unittest

from server_log import Logger


class MyTestCase(unittest.TestCase):

    def test_pxu_startup(self):
        with self.assertLogs() as captured:
            Logger().pxu_start(5)
        self.assertEqual(captured.output[0], 'INFO:root: Connecting to PXU Controller id=5')

    def test_pxu_close(self):
        with self.assertLogs() as captured:
            Logger().pxu_stop(5)
        self.assertEqual(captured.output[0], 'INFO:root: Disconnected from PXU Controller id=5')


if __name__ == '__main__':
    unittest.main()
