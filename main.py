import logging
import time 

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

    

def multiply(a, b):
    logging.info(f" Multiplication: {a} * {b}")
    
    start_time = time.time()  # Get the start time
    end_time = time.time()  # Get the end time
    execution_time = end_time - start_time
    logging.info(f"Execution Time: {execution_time:.6f}")

    try:
        result = a * b
    except NameError:
        logging.error("All the variables should be defined.")
    except IndexError:
        logging.error("Calculation problem")
    else:
        logging.debug(f"Result: {result}")
        return result
    

def test_time_function():
    # Test with a known function
    result, exec_time = time_function(multiply, 1000000)
     
logging.info("The program started")

multiply(10, 5)
multiply(4, 6)
multiply(8,7)

logging.warning("This is a warning")
logging.info("The program ended")