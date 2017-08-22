def abbreviate(phrase):
    
    d ={}
    i = 0
    acronym = ''
    
    #convert phrase to a dictionary     
    
    for c in phrase:
        
        d[i]=c
        i += 1
        
    for c in d:
        
        if c  == 0:
            acronym = d[c]
        elif d[c] == ' ' or d[c] =='-' or d[c] == ',':
            if d[c+1] != ' ' and d[c+1] !='-' and d[c+1] != ',':
                acronym = acronym + d[c+1]
        
    
    return (acronym.upper()) 
    
        
         
    
