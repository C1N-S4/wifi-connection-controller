import speedtest
from datetime import datetime
import time

print("Start")

st = speedtest.Speedtest()

timestamp_format = '%Y-%m-%d %H:%M:%S'

while True:
    timestamp = datetime.now().strftime(timestamp_format)

    download_speed = st.download()
    upload_speed = st.upload()

    print(f'{timestamp}: Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps')

    with open('speed_log.txt', 'a') as f:
        f.write(f'{timestamp},{download_speed:.2f},{upload_speed:.2f}\n')

    time.sleep(60)

print("The end")
