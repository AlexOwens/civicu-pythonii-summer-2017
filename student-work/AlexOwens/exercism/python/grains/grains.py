def on_square(num):
    
    
    if (num <= 0) or (num > 64) or (type(num) == float): 
        raise ValueError('not a valid square number')
    
    on_sqr = 2**(num-1)
    
    return on_sqr


def total_after(num):

    
    if (num <= 0) or (num > 64) or (type(num) == float): 
        raise ValueError('not a valid square number')
    total = 0
    
    for sqr in range(num):
        total = total + 2**(sqr)

    return total

