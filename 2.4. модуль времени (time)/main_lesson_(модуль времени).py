"""
-----------------------------------------------------------------------------------------------------------
время модуль времени
---------------------------------------------------------------------------------------------------------
"""


import time

current_time = time.time()
formated_time = time.ctime(current_time)

print(current_time)
print(formated_time)
#_________________________

import time

current_time = time.time()
local_time = time.localtime(current_time)
gm_time = time.gmtime(current_time)

print(gm_time)


#_________________________форматирование структуры времени

import time

current_time = time.time()
local_time = time.localtime(current_time)

formated_time = time.strftime("%Y-%m-%d %H:%M:%S") #задание формата

print(formated_time )

#_________________________ строки времени

time_string = "2025-01-01 12:00:00"
format_string = "%Y-%m-%d %H:%M:%S"

parsed_time = time.strptime(time_string, format_string)

print(parsed_time)

#_________________________задержка по времени
import time
print(1)
time.sleep(3)
print(2)

#_________________________подсчёт времени

import time

start = time.time()

print("1111111111111")
print("1111111111111")
print("1111111111111")
elapsed = time.time() - start
print(elapsed)

import time

def my_func():
    time.sleep(2)
    print("функция выполнена!")

start_time = time.time()
my_func()
end_time = time.time()

exe_time = end_time - start_time
print(f"{exe_time:.4f}")





