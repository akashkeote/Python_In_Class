#timing function execution 
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)#main ye hai
        end=time.time()
        print(f"Function {func.__name__} took {end-start} seconds to execute.")
        return result
    return wrapper
@timer
def example_function(n):
    time.sleep(n)

example_function(2)  

#create a decorator to print the fun name and values of the agrument every time the function is called
