import multiprocessing as mp
def job(a, b):
        print("Leecheer's first test in Multiprocessing job")

if __name__ == '__main__' :
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()
