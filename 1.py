import threading

class MyThread(threading.Thread):
    def __init__(self, n, pool):
        super(MyThread, self).__init__()
        self.n = n
        self.pool = pool

    def run(self):
        print(f"Calculando 2^{self.n+1} y 2^{10-self.n}")
        self.pool.append(2**(self.n+1) + 2**(10-self.n))



if __name__ == "__main__":
    threads = []
    results = []
    for i in range(5):
        t = MyThread(i, results)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()

    print(results)
    sum = sum(results)

    print(f"Result: {sum}")