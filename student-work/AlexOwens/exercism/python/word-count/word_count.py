

def word_count(some_str):
    
    d ={}
   
    
    for word in some_str.split():
        
        new_word = ''
        word = word.lower()
        
        for c in word:
            
            if c.isalnum() == False:
                if c in ('!','&','@','$','%','^'):
                    break
                elif c in (',','.','_'):
                    word = new_word
                    if word in d and word != '':
                        d[word] = d[word] + 1
                    elif word != '':
                        d[word] = 1
                new_word= ''  
                continue
            
            else:
                new_word = new_word + c
                
        word = new_word
       
        if word in d and word != '':
            d[word] = d[word] + 1
        elif word != '':
            d[word] = 1

    return d
    


 
    




























