def slice_advanced():
    # Código a implementar utilizando input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
    
   text = input("ingrese un texto: ")
   text=text.lower() 
   print(text[4::2])
    
if __name__ == '__main__':
    slice_advanced()
