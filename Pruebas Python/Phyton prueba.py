def code_challenge_one(list, S):
    # Creamos una nueva lista para almacenar los resultados
    result = []
    
    for num in list:
        # Convertimos cada número a una cadena para procesar los dígitos
        num_str = str(num)
        # Guardamos los dígitos que son menores que S
        new_num_str = ''.join([d for d in num_str if int(d) < S])
        
        # Ingreasmos el número a la lista de resultados solo si no está vacío
        if new_num_str:
            new_num = int(new_num_str)
            result.append(new_num)
    
    # Imprimimos el resultado en la consola en en orden contrario
    print(result[::-1])

# Datos
list_num = [80, 68, 5, 4, 3, 2, 8, 7, 9, 29, 18,6,88]
S = 8
# Llamamos la funcion
code_challenge_one((list_num),S)
