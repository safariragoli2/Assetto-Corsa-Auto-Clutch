import pyvjoy
import time

VirtualClutch = pyvjoy.VJoyDevice(1)

VirtualClutch.set_axis(pyvjoy.HID_USAGE_X, 0)
time.sleep(5)
VirtualClutch.set_axis(pyvjoy.HID_USAGE_X, 32768)
