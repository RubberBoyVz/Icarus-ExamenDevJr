# Escribe una función en Python que reciba una lista de números y devuelva una nueva lista con los números ordenados de menor a mayor.

def orderNumbers(list):
    return sorted(list);


numbersList = [1,2,23,2,1,2,4];

print(numbersList);

newNumbersList = orderNumbers(numbersList);

print(newNumbersList);

