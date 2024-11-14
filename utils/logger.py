def log_to_file(log_file, message):
    with open(log_file, "a") as log:
        log.write(message)