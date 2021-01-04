# Incase you messed up the screen position, you can use this script to put it back in place

import win32api
import win32con

def change_display_direction(angle):
    device = win32api.EnumDisplayDevices(None,0)
    dm = win32api.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
    if angle == 90:
        dm.DisplayOrientation = win32con.DMDO_90#To be changed
        #The following 720 or 1280 represents the length and width of my screen
        #When applying the project, it is recommended to use GetSystemMetrics to dynamically obtain the length and width
        #Every time you change the direction, you must judge whether you need to swap the length and width of the screen
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 720: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
     
    elif angle == 180:
        dm.DisplayOrientation = win32con.DMDO_180
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 1280: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

    elif angle == 270:
        dm.DisplayOrientation = win32con.DMDO_270
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 720: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

    elif angle == 0:
        dm.DisplayOrientation = win32con.DMDO_DEFAULT
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 1280: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    
    win32api.ChangeDisplaySettingsEx(device.DeviceName,dm)

change_display_direction(0)
