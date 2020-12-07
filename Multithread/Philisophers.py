import threading
import random
import time

withDeadlock = False


class Philosopher(threading.Thread):
    def __init__(self, name, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = name
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while True:
            print('{0} is thinking.'.format(self.name))
            time.sleep(random.uniform(3, 13))
            print('{0} is hungry.'.format(self.name))
            self.tryGetForks()

    def tryGetForks(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while True:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            if withDeadlock is False:
                fork1.release()
                print('{0} changes priority '.format(self.name))
                fork1, fork2 = fork2, fork1
            else:
                print('{0} waiting for fork '.format(self.name))

        self.eating()
        fork2.release()
        fork1.release()

    def eating(self):
        print('{0} starts eating'.format(self.name))
        time.sleep(random.uniform(1, 10))
        print('{0} finishes eating and leaves to think'.format(self.name))


def testDiner():
    forks = [threading.Lock() for n in range(5)]
    names = ('Seba', 'Konrad', 'Jarek', 'Klaudia', 'Patryk')
    philosophers = [Philosopher(names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    random.seed(123456)
    for p in philosophers:
        p.start()


if __name__ == "__main__":
    testDiner()
