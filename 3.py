import threading
import numpy as np
import math

class MyThread(threading.Thread):
    def __init__(self, n, pool, vector):
        super(MyThread, self).__init__()
        self.n = n
        self.pool = pool
        self.vector = vector

    def run(self):
        print(f"Calculando {self.vector[self.n]}^2 y {self.vector[19-self.n]}^2")
        self.pool.append(self.vector[self.n]**2 + self.vector[19-self.n]**2)



if __name__ == "__main__":
    threads = []
    results = []
    np.random.seed(0)
    vector = np.random.randint(1, 101, 20)
    print(vector)
    for i in range(10):
        t = MyThread(i, results, vector)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()

    print(results)
    sum = sum(results)

    print(f"Suma: {sum}")

    Norma = math.sqrt(sum)
    print(f"Norma Hilos: {Norma}")

    NormaOficial = np.linalg.norm(vector)
    print(f"Norma Oficial: {NormaOficial}")