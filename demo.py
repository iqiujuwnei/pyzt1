#注释

import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)
def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + "at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        # t = MyThread(loop, loops[i], loop.__name__)
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for k in nloops:
        threads[k].start()
    for n in nloops:
        threads[n].join()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()
