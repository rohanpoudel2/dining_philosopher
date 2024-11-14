import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, states, state_lock):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.states = states 
        self.state_lock = state_lock  
        self.state = "Thinking"  

    def run(self):
        while True:
            self.think()
            self.hungry()
            self.try_to_eat()

    def think(self):
        self.update_state("Thinking")
        time.sleep(random.uniform(1, 3))

    def hungry(self):
        self.update_state("Hungry")
        time.sleep(random.uniform(1, 2))

    def try_to_eat(self):
        self.left_fork.acquire()
        self.update_state("Hungry (Left fork picked)")
    
        time.sleep(2)
  
        self.right_fork.acquire()
        self.update_state("Eating")
        time.sleep(random.uniform(1, 2))
    
        self.left_fork.release()
        self.right_fork.release()
        self.update_state("Thinking")

    def update_state(self, new_state):
        with self.state_lock:
            self.state = new_state
            self.states[self.index] = new_state
        print(f"Philosopher {self.index} is {new_state}")

def detect_deadlock(states, state_lock):
    while True:
        time.sleep(5)  
        with state_lock:
            if all(state == "Hungry (Left fork picked)" for state in states):
                print("DEADLOCK DETECTED! All philosophers are stuck.")
                break

def main():
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    states = ["Thinking"] * num_philosophers  
    state_lock = threading.Lock()  
    philosophers = []

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = Philosopher(i, left_fork, right_fork, states, state_lock)
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

    deadlock_detector = threading.Thread(target=detect_deadlock, args=(states, state_lock, num_philosophers))
    deadlock_detector.start()

if __name__ == "__main__":
    main()