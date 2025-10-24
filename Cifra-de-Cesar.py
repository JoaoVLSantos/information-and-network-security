def cifra_cesar(text, keys=3, sort="encrypt"):
    result = ""  
    
    sort = sort.lower()  
    
    if sort == "encrypt" or sort == "e":
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + keys) % 26 + base)
            else:
                result += char  
    elif sort == "decrypt" or sort == "d":
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - keys) % 26 + base)
            else:
                result += char
    # Criar tratamento de erro.
    
    return result
    
# Fazer modelagem, um arquivo main e um arquivo para as funções    
mensagem = input(str("Escreva uma mensagem: "))
keys = int(input("Determine o valor de deslocamento (padrão = 3): ") or 3)
sort = str(input("Determine a operação (por padrão o valor é encrypt, mas pode mudar para decrypt): ") or "encrypt")


mensagem_decifrada = cifra_cesar(mensagem, keys, sort)

print("Mensagem original:   ", mensagem)
print("Mensagem cifre de cesar:  ", mensagem_decifrada)
