import time
import psutil
import os

# Директория для хранения логов
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Определение пути к файлу для записи логов
log_filename = os.path.join(logs_dir, f'system_load_{int(time.time())}.txt')

# Мониторим систему в течение 10 секунд
monitoring_duration = 10  # секунды
end_time = time.time() + monitoring_duration

while time.time() < end_time:
    # Получаем данные о загрузке системы
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    # Записываем данные в файл логов
    with open(log_filename, 'a') as log_file:
        log_file.write(f'Timestamp: {time.ctime()}\n')
        log_file.write(f'CPU Load: {cpu_percent}%\n')
        log_file.write(f'Memory Usage: {memory_percent}%\n')
        log_file.write('\n')  # Разделитель между записями

    time.sleep(1)  # Пауза в 1 секунду между измерениями

print(f'Мониторинг завершен. Результаты сохранены в файл: {log_filename}')
