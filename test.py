import requests
import random
from threading import Thread
from datetime import timedelta
import json
from multiprocessing.dummy import Pool
import time



def func():
    delta = timedelta(days=0,
                           seconds=0,
                           microseconds=0,
                           milliseconds=5,
                           minutes=0,
                           hours=0,
                           weeks=0)
    count_of_fail = 0
    for i in range(100):
        res = requests.get('http://localhost:8080/employees')
        print(res)
        if (res.elapsed > delta):
            count_of_fail += 1
    print(count_of_fail)

def func2(url_adr, elspse_limit, users_count):


    futures =[]
    pool = Pool(users_count)
    print()
    for x in range(users_count):
        futures.append(pool.apply_async(requests.get, [url_adr]))
    res =[]
    result = []
    count_of_fail = 0
    print()
    start_time = time.time()
    for future in futures:
        res.append(future.get())
        #print(res)
    print()
    restime = time.time() - start_time
    for re in res:
        print(re.elapsed.total_seconds())
        if (re.elapsed.total_seconds() > elspse_limit):
            count_of_fail += 1
    print()


    for te in result:
        print(te.total_seconds())#отладочная информация

    print(count_of_fail)
    print(count_of_fail/(users_count/100))
    return restime #отладочная информация





#test = func()

test = func2('http://localhost:8080/employees', 0.9, 1000)


#
# res = requests.post('http://localhost:8080/employees',
#                     headers = {
#                                 'Content-Type': 'application/json'
#                             },
#                     data = json.dumps({
#                             "deptNo" : 1,
#                             "firstName" : "Test",
#                             "lastName" : "Employee",
#                             "hireDate" : "2021-09-21",
#                             "salary" : 1000.0
#                     }))
