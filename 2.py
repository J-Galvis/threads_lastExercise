import threading

class MyThread(threading.Thread):
    def __init__(self, operation, n1, n2, results, index):
        super(MyThread, self).__init__()
        self.operation = operation
        self.n1 = n1
        self.n2 = n2
        self.results = results
        self.index = index

    def run(self):
        if self.operation == "suma":
            self.results[self.index] = self.suma(self.n1, self.n2)
        elif self.operation == "resta":
            self.results[self.index] = self.resta(self.n1, self.n2)
        elif self.operation == "multi":
            self.results[self.index] = self.multi(self.n1, self.n2)
        elif self.operation == "divi":
            self.results[self.index] = self.divi(self.n1, self.n2)

    def suma(self, p, q):
        return p + q
    
    def resta(self, p, q):
        return p - q
    
    def multi(self, p, q):
        return p * q
    
    def divi(self, p, q):
        return p / q if q != 0 else "Error: División por cero"

if __name__ == "__main__":
    n1, n2 = 10, 5  # Puedes cambiar estos valores
    operations = ["suma", "resta", "multi", "divi"]
    results = [None] * len(operations)  # Lista para almacenar los resultados
    threads = []
    
    for i, op in enumerate(operations):
        t = MyThread(op, n1, n2, results, i)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("Resultados:", results)
