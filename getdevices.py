from ppadb.client import Client

# class devices:
#     def __init__(self) -> None:
#         pass
#     def getdevices():
#         client= Client(host="127.0.0.1", port=5037)
#         devices = client.devices()
#         # if len(devices)<0:
#         #     return "Not find any devices"
#         return devices
    
# devices1 = devices.getdevices()
# for device in devices1:
#     print(device)


import subprocess
class check_devices:
    def __init__(self) -> None:
        pass
    def check_devices():
        output = subprocess.check_output("adb devices")
        string= output.decode()
        substring = "List of devices attached"
        substrings = string.replace(substring,"")
        substring = "device"
        substrings2 = substrings.replace(substring,"")
        return substrings2.strip().split()
        # print(type(output))
    def check_devices2():
        output = subprocess.check_output("adb devices -l")
        string= output.decode()
        substring = "List of devices attached"
        substrings = string.replace(substring,"")
        print(substrings.split("    "))
        # substring = "device"
        # substrings2 = substrings.replace(substring,"")
        # return substrings2.strip().split()
        # print(type(output))

# a=check_devices.check_devices2()
# print(a)