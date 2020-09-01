def elefantes(n, minimo=1):
    if n >= minimo+1:
        string = ""
        if minimo == 1:
            string += str(minimo)+" elefante incomoda muita gente\n"
        else:
            string += str(minimo)+ " elefantes incomodam muita gente\n"
        string += str(minimo+1) + " elefantes" + incomodam(minimo+1) + " muito mais\n"

        return string + elefantes(n,minimo+1)
    else:
        return ""

def incomodam(numero):
    string2 = ""
    while numero > 0:
        string2 +=" incomodam,"
        numero -= 1
    return string2


        
    
