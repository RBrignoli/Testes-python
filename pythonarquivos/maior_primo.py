def maior_primo(n):

    p = n
    a = 2
    while a != p:
        if p % a == 0:
            p -= 1
            a = 2
        else:
            a += 1
            
    return(p)
                
                
                

        
 
        
        
        

               
