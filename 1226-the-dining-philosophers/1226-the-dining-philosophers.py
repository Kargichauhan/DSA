from threading import Lock
from typing import Callable


class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: 'Callable[[], None]',
        pickRightFork: 'Callable[[], None]',
        eat: 'Callable[[], None]',
        putLeftFork: 'Callable[[], None]',
        putRightFork: 'Callable[[], None]'
    ) -> None:

        left = philosopher
        right = (philosopher + 1) % 5

        first = min(left, right)
        second = max(left, right)

        with self.forks[first]:
            with self.forks[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()