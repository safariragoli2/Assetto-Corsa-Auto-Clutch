import sys
import ac
import acsys
import pyvjoy

VirtualClutch = pyvjoy.VJoyDevice(1)

def acMain(ac_version):
    appWindow = ac.newApp("Auto Clutch")
    ac.setSize(appWindow, 250, 100)
    text = ac.addLabel(appWindow, "Simply having the app itself enabled\nwill enable the auto clutch, no need\nto have this UI enabled.")
    ac.setPosition(text, 3,30)
    
    return "Auto Clutch"

def acUpdate(deltaT):
    currentGear = ac.getCarState(0, acsys.CS.Gear)
    
    if currentGear == 1: # neutral
        VirtualClutch.set_axis(pyvjoy.HID_USAGE_X, 32768) # clutch on
    else:
        VirtualClutch.set_axis(pyvjoy.HID_USAGE_X, 0) # clutch off
