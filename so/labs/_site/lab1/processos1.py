from multiprocessing import Pool
import time

def ola(n):
    time.sleep(10)
    print("ola "+str(n))

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(ola, [1])
    r2 = pool.apply_async(ola, [2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
