from base_philosopher import Philosopher
import time

class PhilosopherDeadlock(Philosopher):
    def try_to_eat(self):
        self.left_fork.acquire()
        self.update_state("Hungry (Left fork picked)")
        time.sleep(2) 
        self.right_fork.acquire()
        self.update_state("Eating")
        time.sleep(2)
        self.left_fork.release()
        self.right_fork.release()
        self.update_state("Thinking")