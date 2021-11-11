
from typing import Callable

def estimate_function(func: Callable):
    import time
    
    start_time = time.time()
    func()
    print("\x1b[0;30;47m{0}\x1b[0m: {1:.6f} seconds!".format(func.__name__, time.time() - start_time))
    del start_time
