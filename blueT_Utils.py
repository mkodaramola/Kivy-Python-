#!/usr/bin/python3
# geektechstuff bluetooth
import bluetooth
import psutil as ps
def scan():
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print(number_of_devices,"devices found")
    for addr, name, device_class in devices:
        print("\n")
        print("Device:")
        print("Device Name: %s" % (name))
        print("Device MAC Address: %s" % (addr))
        print("Device Class: %s" % (device_class))
        print("\n")
    return










battery = ps.sensors_battery()


print ("Percentage:", (battery.percent))

print ("Seconds left:", (battery.secsleft))

print ("Seconds left:", battery.power_plugged)

print (ps.virtual_memory())




# pr = ps.pids()

# for i in pr:
#     name = ps.Process(i)
#     print(name.username)





