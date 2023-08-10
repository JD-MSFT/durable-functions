# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import time

def main(name: str) -> str:
    # update the range and sleep variables to test longer running functions
    logging.info(f"going into main!!! {name}")
    for i in range(2):
        logging.info(f"Hello {name}! {i}")
        time.sleep(5)
    return f"Hello {name}!"
