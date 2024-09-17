import threading 
import time

def worker(thread_num):
    print("Função chamada pela thread n %i começando\n" % thread_num)

    time.sleep(5)
    print("Aguardando a thread %i acabar...\n" % thread_num)

def exec():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for i in threads:
        i.join
        
    print("Acabou!!!")

if __name__ == "__main__":
    exec() 