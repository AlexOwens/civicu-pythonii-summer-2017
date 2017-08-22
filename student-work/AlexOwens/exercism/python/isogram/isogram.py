def is_isogram(some_word):
    
    
    char_list = []
    
#populates a list with all the characters in a phrase and returns false if it appears twice 
    
    for c in some_word.lower():
        
        if c in char_list and c.isalpha():
            return False
            
        else:
            char_list.append(c)
            
        
    return True

