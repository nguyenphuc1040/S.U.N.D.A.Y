import time
from multiprocessing import Process
from Sunday import daemon

class MultiProcess(object):
    def __init__(self, num_process=4, num_op=100):
        self.num_process = num_process
        self.num_op = num_op
        assert self.num_process > 0
        assert self.num_op > 0
        pass

    def __call__(self):
        process_list = []
        for _ in range(self.num_process):
            p = Process(target=daemon, args=(self.num_op,))
            p.start()
            process_list.append(p)

        for _ in range(len(process_list)):
            p = process_list[_]
            p.join()

        pass
    
def main(num_cpus=4, num_ops=10):
    tstart = time.time()
    multi = MultiProcess(num_process=num_cpus, num_op=num_ops)
    multi()
    tend = time.time()

    
if __name__ == "__main__":
    main() 