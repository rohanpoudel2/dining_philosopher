from base_philosopher import Philosopher
import time

class PhilosopherResourceHierarchy(Philosopher):
    def try_to_eat(self):
        first_fork, second_fork = (self.left_fork, self.right_fork) if self.index % 2 == 0 else (self.right_fork, self.left_fork)
        first_fork.acquire()
        self.update_state("Hungry (Picked first fork)")
        time.sleep(1)
        second_fork.acquire()
        self.update_state("Eating")
        time.sleep(2)
        first_fork.release()
        second_fork.release()
        self.update_state("Thinking")