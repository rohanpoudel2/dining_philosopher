from base_philosopher import Philosopher
import time

class PhilosopherCheckBothForks(Philosopher):
    def try_to_eat(self):
        while True:
            if self.left_fork.acquire(timeout=1):
                if self.right_fork.acquire(timeout=1):
                    self.update_state("Eating")
                    time.sleep(2)
                    self.left_fork.release()
                    self.right_fork.release()
                    self.update_state("Thinking")
                    break
                else:
                    self.left_fork.release()
            self.update_state("Hungry (Retrying)")
            time.sleep(1)