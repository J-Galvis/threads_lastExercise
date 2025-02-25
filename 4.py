import threading
import math

class MyThread(threading.Thread): # threading.Thread es la clase base para crear hilos
    def __init__(self, start:int, end:int, pool:list, lock = threading.Lock()):
        '''
        threading.Lock(): Me asegura de que solo se escriba un hilo a la vez en la lista pool
        start: Inicio del rango de números a sumar
        end: Fin del rango de números a sumar
        '''
        super(MyThread, self).__init__()
        self.start_range = start
        self.end_range = end
        self.pool = pool
        self.lock = lock

    def run(self):
        suma_parcial = sum(math.factorial(i) for i in range(self.start_range, self.end_range + 1))
        with self.lock: 
            '''with se usa para el manejo de excepciones, la declaración with en sí misma garantiza 
            la adquisición y liberación adecuadas de los recursos. '''
            self.pool.append(suma_parcial)

if __name__ == "__main__":
    n = int(input("Ingrese el valor de n: "))
    num_hilos = int(input("Ingrese la cantidad de hilos: "))
    
    threads = []
    results = []
    
    chunk_size = n // num_hilos
    extra = n % num_hilos
    inicio = 1
    
    for i in range(num_hilos):
        fin = inicio + chunk_size - 1 #Dertermina el número final del rango
        if extra > 0: # En caso de que sobren números, los primero hilos se encargaran de ellos.
            fin += 1
            extra -= 1
        
        t = MyThread(inicio, fin, results)
        t.start()
        threads.append(t)
        
        inicio = fin + 1
    
    for t in threads:
        t.join()
    
    resultado_total = sum(results)
    print(f"La suma de los factoriales de 1! a {n}! es: {resultado_total}")
