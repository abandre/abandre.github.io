
import time, os 
from threading import Thread, current_thread 
from multiprocessing import Process, current_process, Pool
import sys
  
COUNT = 200000000
SLEEP = 10
  
def io_bound(sec): 
  
    pid = os.getpid() 
    threadName = current_thread().name 
    processName = current_process().name 
  
    #print(f"{pid} * {processName} * {threadName} ---> Start sleeping...") 
    print(pid," * ",processName," * ",threadName," ---> Start sleeping...") 
    time.sleep(sec) 
    print(pid," * ",processName," * ",threadName," ---> Finish sleeping...") 
    #print(f"{pid} * {processName} * {threadName} ---> Finished sleeping...") 
  
def cpu_bound(n): 
  
    pid = os.getpid() 
    threadName = current_thread().name 
    processName = current_process().name 
  
    print(f"{pid} * {processName} * {threadName} ---> Start counting...") 
  
    while n>0: 
        n -= 1
  
    print(f"{pid} * {processName} * {threadName} ---> Finished counting...") 
  
if __name__=="__main__": 
    start = time.time() 
  
    if len(sys.argv)!=2:
        print("USO: python lab3.py DEBUG")
        sys.exit(1)

    DEBUG=int(sys.argv[1])
    
    if DEBUG==1:
        io_bound(SLEEP) 
        io_bound(SLEEP) 
    elif DEBUG==2:
        t1 = Thread(target = io_bound, args =(SLEEP, )) 
        t2 = Thread(target = io_bound, args =(SLEEP, )) 
        t1.start() 
        t2.start() 
        t1.join() 
        t2.join() 
    elif DEBUG==3:
        cpu_bound(COUNT) 
        cpu_bound(COUNT) 
    elif DEBUG==4:
        t1 = Thread(target = cpu_bound, args =(COUNT, )) 
        t2 = Thread(target = cpu_bound, args =(COUNT, )) 
        t1.start() 
        t2.start() 
        t1.join() 
        t2.join() 
    elif DEBUG==5:
        p1 = Process(target = cpu_bound, args =(COUNT, )) 
        p2 = Process(target = cpu_bound, args =(COUNT, )) 
        p1.start() 
        p2.start() 
        p1.join() 
        p2.join() 
    elif DEBUG==6:
        pool = Pool(processes=2)
        pool.apply_async(cpu_bound, [COUNT])
        pool.apply_async(cpu_bound, [COUNT])
        pool.close()
        pool.join()
    elif DEBUG==7:
        p1 = Process(target = io_bound, args =(SLEEP, )) 
        p2 = Process(target = io_bound, args =(SLEEP, )) 
        p1.start() 
        p2.start() 
        p1.join() 
        p2.join() 
  
    end = time.time() 
    print('Time taken in seconds -', end - start) 
