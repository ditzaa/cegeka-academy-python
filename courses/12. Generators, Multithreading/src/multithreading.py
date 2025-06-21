import time
from threading import Thread


def hello():
    time.sleep(2)
    print("Hello from another thread")


class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Hello World!")


if __name__ == "__main__":
    t = Thread(group=None, target=hello)
    t.start()
    t2 = MyThread()
    t2.start()
    print("Main thread ended")
