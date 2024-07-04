def  code_challenge_three (coins):
    # Ordenamos las monedas
    coins.sort()  

    # Inicializamos la suma mínima no posible como 1
    min_sum = 1
    
    # Sumamos las monedas ordenadas
    for coin in coins:
        # Si la moneda actual es mayor que la suma mínima no posible, entonces la suma mínima no posible es la respuesta
        if coin > min_sum:
            return min_sum
        
        # Sumamos la moneda actual a la suma minima
        min_sum += coin
    
    # En caso de haber recorrido todas las monedas y no haber superado la suma minima la respuesta sera 1
    return min_sum

# Llamamos la funcion y ingresamos las monedas
print(code_challenge_three ([1, 2, 3, 5, 7]))  
print(code_challenge_three ([1, 3, 8, 5, 6, 10 ]))  
print(code_challenge_three ([3, 5, 7, 9]))  
