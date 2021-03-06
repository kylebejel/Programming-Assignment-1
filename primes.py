import threading
import time
import sys

class myThread (threading.Thread):
   def __init__(self, begin):
      threading.Thread.__init__(self)
      self.begin = begin
   def run(self):
      threadLock.acquire()
      thread_sieve(self.begin)
      threadLock.release()

def thread_sieve(x):
    for y in range(x*x, 100000000, x):
        bools[y] = False

bools = [True] * 100000000
thread_counter = 0
threads = []
threadLock = threading.Lock()
primes = []
start_time = time.time()
for x in range(2, 10000):
    if bools[x]:
        if thread_counter >= 8:
            for t in threads:
                t.join()
                thread_counter = 0
        if thread_counter < 8:
            thread_counter+=1
            tmp = myThread(x)
            tmp.start()
            threads.append(tmp)

for x in range(2, len(bools)):
    if bools[x]:
        primes.append(x)

with open('primes.txt', 'w') as fp:
    sys.stdout = fp
    print("RUN TIME: %s SECONDS" % (time.time() - start_time))
    print("NUM OF PRIMES: %s" % len(primes))
    print("SUM OF PRIMES: %s" % sum(primes))
    print("MAX 10 PRIMES: %s" % sorted(primes)[-10:])


