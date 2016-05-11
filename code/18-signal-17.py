#coding=utf-8
import threading
import time


class Semaphore(object):
    def __init__(self, sem):
        super(Semaphore, self).__init__()
        self.sem = sem
        self.cv = threading.Condition()

    def p(self):
        self.cv.acquire()
        self.sem -= 1
        if self.sem < 0:
            self.cv.wait()
        self.cv.release()

    def v(self):
        self.cv.acquire()
        self.sem += 1
        if self.sem <= 0:
            self.cv.notify(n=1)
        self.cv.release()


def driver(sem_drive, sem_opendoor):
    while (True):
        sem_drive.p()
        print("Started")
        print("Driving")
        time.sleep(1)
        print("Stop")
        sem_opendoor.v()


def conductor(sem_drive, sem_opendoor):
    while (True):
        print("\tDoor closed")
        sem_drive.v()
        print("\tConducting")
        sem_opendoor.p()
        print("\tDoor Opened")
        print("\tOn & Off")
        time.sleep(1)


def main():
    sem_drive = Semaphore(0)
    sem_opendoor = Semaphore(0)

    print("Driver\tConductor")
    thread_driver = threading.Thread(target=driver, name="driver", args=(sem_drive, sem_opendoor))
    thread_conductor = threading.Thread(target=conductor, name="conductor", args=(sem_drive, sem_opendoor))

    thread_driver.start()
    thread_conductor.start()

    thread_driver.join()
    thread_conductor.join()

if __name__ == "__main__":
    main()
