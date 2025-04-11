def check_vowels():
    # Código a implementar utilizando input.

    # Para verificar este ejercicio ejecutar el comando
    # `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

    name=input("cual es tu nombre?: ")
    name=name.lower()
    if "a" in name:
        print("Contiene a: True")
    else:
        print("Contiene a: False")
      
    if "e" in name:
        print("Contiene e: True")    
    else:
        print("Contiene e: False")
        
    if "i" in name:
        print("Contiene i: True")   
    else:
        print("Contiene i: False")
        
    if "o" in name:
        print("Contiene o: True")
    else:
        print("Contiene o: False")
        
    if "u" in name:    
        print("Contiene u: True")    
    else:
        print("Contiene u: False")
check_vowels()
