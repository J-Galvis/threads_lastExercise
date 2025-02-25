import threading
import math

class MyThread(threading.Thread):
    def __init__(self, start, end, pool, lock):
        super(MyThread, self).__init__()
        self.start_range = start
        self.end_range = end
        self.pool = pool
        self.lock = lock

    def run(self):
        suma_parcial = sum(math.factorial(i) for i in range(self.start_range, self.end_range + 1))
        with self.lock:
            self.pool.append(suma_parcial)

if __name__ == "__main__":
    n = int(input("Ingrese el valor de n: "))
    num_hilos = int(input("Ingrese la cantidad de hilos: "))
    
    threads = []
    results = []
    lock = threading.Lock()
    
    chunk_size = n // num_hilos
    extra = n % num_hilos
    inicio = 1
    
    for i in range(num_hilos):
        fin = inicio + chunk_size - 1
        if extra > 0:
            fin += 1
            extra -= 1
        
        t = MyThread(inicio, fin, results, lock)
        t.start()
        threads.append(t)
        
        inicio = fin + 1
    
    for t in threads:
        t.join()
    
    resultado_total = sum(results)
    print(f"La suma de los factoriales de 1! a {n}! es: {resultado_total}")
