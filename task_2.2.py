import psutil
import time

memory = psutil.virtual_memory()
dick_usage = psutil.disk_usage("/")
while True:
    output_1 = f"""Нагрузка CPU: {psutil.cpu_percent(interval=1)}% 
использовано оперативной памяти: {memory.used/(1024**3):.2f} ГБ 
процентное использование жесткого диска: {dick_usage.percent:.1f}%
"""
    print(output_1)
    #print("\n")
    time.sleep(3)
