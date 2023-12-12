import os
import time

log_dir = "logs"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "system_load.log")

monitoring_interval = 10

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    cpu_load = os.getloadavg()[0]
    with open(log_file, "a") as f:
        f.write(f"{current_time}: CPU Load: {cpu_load}\n")
    time.sleep(monitoring_interval)
