from getdevices import check_devices
import os, threading 
from time import sleep
class openss:
    def __init__(self, device=None) -> None:
        # self.udid = udid
        self.device =device
    def open_app(self, package):
        # os.system(f"adb -s {self.device} shell monkey -p com.sec.android.app.shealth 1")
        os.system(f"adb -s {self.device} shell monkey -p {package} 1")
        # sleep(5)
    def close_app(self, package):
        os.system(f"adb -s {self.device} shell pm clear {package} 1")
    def close_app2(self, package):
        os.system(f"adb -s {self.device} am force-stop {package}")
    def search_chrome(self, text):
        self.open_app(package="com.android.chrome")
        os.system(f"adb -s {self.device} shell input keyevent 84")
        os.system(f"adb -s {self.device} shell input text {text}")
        os.system(f"adb -s {self.device} shell input keyevent 66")
    def run(self):
       
        # sleep(8)
        # self.close_app(package="com.android.chrome")

        self.open_app(package="com.facebook.katana")
        sleep(5)
        self.close_app(package="com.facebook.katana")

        self.open_app(package="com.zing.zalo")
        sleep(4)
        self.close_app(package="com.zing.zalo")

        self.open_app(package="com.ss.android.ugc.trill")
        sleep(6)
        self.close_app(package="com.ss.android.ugc.trill")
        self.search_chrome(text="https://www.adb-shell.com/android/logcat.html")
    
       



if __name__=="__main__":
    list_devices = check_devices.check_devices()
    print(list_devices)
    for device in list_devices:
        threading.Thread(target=openss(device=device).run).start()


