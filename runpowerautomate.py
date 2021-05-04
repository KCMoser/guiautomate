
import subprocess
import pyautogui
import time

command = "C:\\Program Files (x86)\\Power Automate Desktop\\PAD.Console.Host.exe"
subprocess.Popen(command)
time.sleep(6)
pyautogui.moveTo(1561, 966)
pyautogui.sleep(2)
pyautogui.click()
time.sleep(3)
pyautogui.click(2692, 553)