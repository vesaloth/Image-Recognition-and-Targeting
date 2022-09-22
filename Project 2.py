import subprocess
import os
import sys

password_file = open('passwords.txt', "w")
password_file.write("Hello sir! Here are your passwords:\n\n")
password_file.close()

wifi_files = []
wifi_name = []
wifi_password = []

command = subprocess.run (["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

path = os.getcwd()


for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep='\n')
                            sys.stdout.close()



















