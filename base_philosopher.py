import threading
from datetime import datetime

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, states, state_lock, log_file):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.states = states 
        self.state_lock = state_lock  
        self.state = "Thinking"  
        self.log_file = log_file 

    def run(self):
        while True:
            self.think()
            self.hungry()
            self.try_to_eat()

    def think(self):
        self.update_state("Thinking")

    def hungry(self):
        self.update_state("Hungry")

    def update_state(self, new_state):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.state_lock:
            self.state = new_state
            self.states[self.index] = new_state
        log_entry = f"{timestamp} - Philosopher {self.index} is {new_state}\n"
        print(log_entry.strip())
        with open(self.log_file, "a") as log:
            log.write(log_entry)

    def try_to_eat(self):
        raise NotImplementedError("This method should be implemented by subclasses.")