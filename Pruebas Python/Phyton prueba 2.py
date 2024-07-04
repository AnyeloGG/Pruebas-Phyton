def code_challenge_two(list, S):

    #Inicializando variables y array
    max_value = S
    squared_array = []
    
    #Operacion para dar el cuadrado sobre cada número en la lista
    for num in list:
        square = num ** 2
        #Ingresar los cuadrados al array que no sean mayores o iguales a SS
        if square <= max_value:
            squared_array.append(square)

    #Ordenar manualmente los numeros en squared_array
    for i in range(len(squared_array)):
        for j in range(i + 1, len(squared_array)):
            if squared_array[i] > squared_array[j]:
                squared_array[i], squared_array[j] = squared_array[j], squared_array[i]
    
    return squared_array

# Datos
list = [-8, -7, -3, 1, 5, 6, 9, 13]
S = 88
# Llamamos la funcion
print(code_challenge_two(list, S))
