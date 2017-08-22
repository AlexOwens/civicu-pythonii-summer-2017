def prime_factors(comp_num):
    
    div = 2
    factors_list = []
    
    while(div <= comp_num):
        
        div = first_prime(comp_num)
        factors_list.append(div)
        comp_num = (comp_num/div)
    return factors_list

    
def first_prime(comp_num):
    
    
    for num in range(int(comp_num)):
        
        div = num + 1

        if (comp_num % div == 0 and div != 1):
            return div
        
        if num == comp_num:
            return num
