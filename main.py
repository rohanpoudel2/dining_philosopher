import threading
from philosopher_deadlock import PhilosopherDeadlock
from philosopher_hierarchy import PhilosopherResourceHierarchy
from philosopher_check import PhilosopherCheckBothForks

def main(simulation_type):
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    states = ["Thinking"] * num_philosophers
    state_lock = threading.Lock()
    philosophers = []
    log_file = "philosophers_log.txt"
    open(log_file, "w").close()  

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]

        if simulation_type == "deadlock":
            philosopher = PhilosopherDeadlock(i, left_fork, right_fork, states, state_lock, log_file)
        elif simulation_type == "resource_hierarchy":
            philosopher = PhilosopherResourceHierarchy(i, left_fork, right_fork, states, state_lock, log_file)
        elif simulation_type == "check_both_forks":
            philosopher = PhilosopherCheckBothForks(i, left_fork, right_fork, states, state_lock, log_file)
        else:
            raise ValueError("Invalid simulation type.")

        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()


if __name__ == "__main__":
    print("Choose a simulation type: 'deadlock', 'resource_hierarchy', or 'check_both_forks'")
    simulation_type = input("Enter simulation type: ").strip().lower()
    main(simulation_type)