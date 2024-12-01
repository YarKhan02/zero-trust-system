import logging

logging.basicConfig(filename='access_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_access(username, action, status):
    """Log user actions to track access."""
    log_message = f"User: {username}, Action: {action}, Status: {status}"
    logging.info(log_message)
    print(log_message)
