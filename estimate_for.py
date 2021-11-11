from time_estimate import estimate_function

ls = [1 for i in range(int(5e6))]


def loop_1():
    i = 0
    for _ in range(len(ls)):
        i += 1
    

def loop_2():
    i = 0
    while i < len(ls):
        i += 1


def loop_3():
    j = 0
    for i, _ in enumerate(ls):
        j += 1
        
   
def loop_4():
    iterator = iter(ls)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            pass
            
  
def loop_5():
    i = 0
    [i + 1 for _ in range(len(ls))]
    
                     
def main():        
    estimate_function(loop_1)
    estimate_function(loop_2)
    estimate_function(loop_3)
    estimate_function(loop_4)
    estimate_function(loop_5)
    

main()