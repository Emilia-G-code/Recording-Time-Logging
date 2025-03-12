import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import time

def time_function(func, *args, **kwargs):
    """Measures the execution time of a function and logs the results."""
    start_time = time.time()  # Get the start time
    result = func(*args, **kwargs)  # Call the function with its arguments
    end_time = time.time()  # Get the end time
    execution_time = end_time - start_time  # Calculate the execution time
    
    # Log the execution time
    logging.info(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
    
    return result, execution_time  # Return the result and the execution time
def sample_function(n):
    """A simple function that simulates some work."""
    total = 0
    for i in range(n):
        total += i
    return total
def test_time_function():
    # Test with a known function
    result, exec_time = time_function(sample_function, 1000000)
    
    # Check if the result is correct
    expected_result = sum(range(1000000))
    assert result == expected_result, "The result is incorrect."
    
    # Check if execution time is reasonable (e.g., less than 1 second)
    assert exec_time < 1, "The function took too long to execute."
    
    logging.info("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_time_function()