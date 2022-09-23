import time
from concurrent.futures import ThreadPoolExecutor


def return_number(num):
    time.sleep(1)
    return num

   
start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor1:
    for result in executor1.map(return_number, range(100)):
        print("count:{0}". format(result))

    print("The Total time is:{0}".format(time.time()-start))