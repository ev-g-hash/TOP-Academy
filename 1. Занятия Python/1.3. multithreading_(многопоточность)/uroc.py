"""
многопоточность
#-------------------------------------------------------------начало
"""
import multiprocessing
import time

# import time
# import threading
#
# def get_data(data):
#     while True:
#         th_name = "aa"
#         print(f"[{th_name}] - {data}")
#         time.sleep(1)
#
# def get_data_1(data):
#     while True:
#         th_name = "aa"
#         print(f"[{th_name}] - {data}")
#         time.sleep(1)
#
# thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1")
# thr_1 = threading.Thread(target=get_data_1, args=(str(time.time()),), name="thr-2")
#
# thr.start()
# thr_1.start()
#
# for i in range(100):
#     print(f"current: - {i}")
#     time.sleep(1)


# import time
# import threading
#
# def get_data(data):
#     while True:
#         print(f"[{threading.current_thread().name}] - {data}")
#         time.sleep(1)
#
# thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1")
# thr.start()
#
# for i in range(50):
#     print(f"current: {i}")
#     time.sleep(1)
#
#
#     if i % 10 == 0:
#         print(f"activ thread:", threading.active_count())        # количество активных потоков
#         print(f"enumerate:", threading.enumerate())                #  какие потоки в работе
#         print(f"thr-1 is activ", thr.is_alive())                # активен ли наш поток
#
#         print(f"name: ", threading.main_thread().name)          # имя на лету
#         # threading.main_thread().setName("result")
#         # print(f"result: ", threading.main_thread().name)

#--------------------------------------------------------------------------

# import time
# import threading
#
# def get_data(data, value):
#     for _ in range(value):
#         print(f"[{threading.currentThread().name}] - {data}")
#         time.sleep(1)
#
# thr_list = []
#
# for i in range(5):
#     thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f"thr-{i}")
#     thr_list.append(thr)
#     thr.start()
#
# print(thr_list)
#
# for i in thr_list:
#     i.join()
#
# print("finih")

"""
#-----------------------------------------------поток демон завершает все потоки
# как только наш завершится
"""

# import time
# import threading
#
# def get_data(data):
#     for i in range(5):
#         thr_name = "A"
#         print(f"[{thr_name}] - {data}")
#         time.sleep(1)
#
# thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
# thr.start()
#
# print("-----finish")

#-------------------------------------------------------------семафоры и барьеры
# пулы потоков

# import threading
# from threading import Thread, BoundedSemaphore
# from threading import currentThread
# import random
#
# max_connections = 5
# pool = BoundedSemaphore(value=max_connections)
#
#
# def proba():
#     while True:
#         with pool:
#             slp = random.randint(1, 5)
#             print(f"{currentThread().name} - sleep {slp}")
#             time.sleep(slp)
#
# for i in range(10):
#     Thread(target=proba, name=f"th-{i}").start()

#---------------------
# from threading import Thread, BoundedSemaphore
#
# max_connections = 3
# pool = BoundedSemaphore(value=max_connections)
#
# def connections_3():
#     with pool:
#         print(f"{connections_3.__name__}")
#         time.sleep(3)
#
#
# for i in range(10):
#     Thread(target=connections_3, name=f"th-{i}").start()

#------------------------------------------------у меня не работает

# import time
# import  multiprocessing
#
# def func():
#     while True:
#
#         print(f"{multiprocessing.current_process().name} - {time.time()}")
#         time.sleep(1)
#
# time.sleep(10)
# multiprocessing.Process(target=func, name="prc-1").start()
#
# print("процесс запущен")
#=======================================================================
# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

"""
https://docs.python.org/3/library/multiprocessing.html
"""
#------------------------------------------------------------


"""
парсинг
"""

# import requests
#
# URL = "https://alex-dein.ru/portfolio/bani/"
# r = requests.get(URL)
# print(r.status_code)
# print(r.text)

# #------------------------------------------------------event True, False
# import time
# from multiprocessing import Process, Event
#
# event = Event()
#
# def prob():
#     print("функция prob запущена")
#     while True:
#         event.set()
#         print("Event True")
#         event.wait()
#         print("prob")
#         time.sleep(3)
#         event.clear()
#         print("Event False")
#
# if __name__ == '__main__':
#     Process(target=prob).start()


#------------------------------------------------------Condition
# import time
# from multiprocessing import Process, Condition
#
# cond = Condition()
#
# # def f1():
# #     while True:
# #         with cond:
# #             cond.wait()
# #             return "получено событие"
#
# def f2():
#     for i in range(100):
#         if i % 10 == 0:
#             with cond:
#                 cond.notify()
#             print("получено событие")
#         else:
#             print(f"f2: {i}")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # Process(target=f1).start()
#     Process(target=f2).start()

#-------------------------------------------------------barrier

import time
import random
from multiprocessing import Process, Barrier

def f1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2, 10)
    print(f"{name} - спим {sl} секунд")
    time.sleep(sl)
    bar.wait()
    print(f"{name} - запущено")

b = Barrier(5)

if __name__ == '__main__':
    for i in range(10):
        Process(target=f1, args=(b,)).start()








