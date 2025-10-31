def algoritmo_euclidiano(a, b):

    if a == 0 or b == 0:
        return max(a, b)
    
    if a == b:
        return a
    
    if a < b:
        a, b = b, a

    quociente = a // b
    resto = a % b
    
    print(f"{a} = {quociente} * {b} + {resto}")
    
    
    if resto == 0:
        return b
        
    else:
        return algoritmo_euclidiano(b, resto)

mdc = algoritmo_euclidiano (987654321234567890, 12345678901234567890)

print (f"mdc = {mdc}")
