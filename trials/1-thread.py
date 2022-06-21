import threading 
counter = 0

lock = threading.RLock()

def func1():
    global counter

    while True:
        with lock:
            counter+=1
            counter-=1
            print("func1: ", counter)

def func2():
    global counter

    while True:
        with lock:
            counter+=1
            counter-=1

            print("func2: ", counter)

threading.Thread(target=func1).start()
threading.Thread(target=func2).start() 