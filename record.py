import speedtest
from datetime import datetime
import time
import os
import csv
import matplotlib.pyplot as plt

print("Start")

st = speedtest.Speedtest()

timestamp_format = '%Y-%m-%d %H:%M:%S'

if os.path.exists('speed_log.txt'):
    with open('speed_log.txt', 'r') as f:
        last_line = f.readlines()[-1]
        last_download_speed = float(last_line.split(',')[1])
        last_upload_speed = float(last_line.split(',')[2])
else:
    last_download_speed = None
    last_upload_speed = None

download_speed_list = []
upload_speed_list = []
timestamp_list = []

for i in range(5):
    timestamp = datetime.now().strftime(timestamp_format)

    download_speed = st.download()
    upload_speed = st.upload()

    download_speed_list.append(download_speed)
    upload_speed_list.append(upload_speed)
    timestamp_list.append(timestamp)

    print(f'{timestamp}: Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps')

    with open('speed_log.txt', 'a') as f:
        f.write(f'{timestamp},{download_speed:.2f},{upload_speed:.2f}\n')

    time.sleep(60)

if last_download_speed is not None and last_upload_speed is not None:
    download_speed_change = ((download_speed - last_download_speed) / last_download_speed) * 100
    upload_speed_change = ((upload_speed - last_upload_speed) / last_upload_speed) * 100

    print(f'Download Speed Change: {download_speed_change:.2f}%, Upload Speed Change: {upload_speed_change:.2f}%')

    fig, ax = plt.subplots()
    ax.plot(timestamp_list, download_speed_list, label='Download Speed')
    ax.plot(timestamp_list, upload_speed_list, label='Upload Speed')
    ax.legend()
    plt.xticks(rotation=45)
    plt.show()

print("The end")
