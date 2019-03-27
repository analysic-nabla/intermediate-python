
def is_amstrong(n):
    """
    Función para validar si un número entero positivo
    es un número de Amstrong
    
    parameters
    ----------
    n: int
        número a validar si es Amstrong
       
    Returns
    -------
    Bool:
        True si 'n' es Amstrong. Falso de otra manera
    """
    numbers = []
    total_sum = 0
    # Obtenemos cada dígito del número
    for ni in str(n):
        numbers.append(ni)
    
    for ni in numbers:
        total_sum = ni
    
    validation = True if total_sum == n else False
    return validation


def amstrong_between(a, b):
    """
    Función para encontrar todos los números
    amstrong entre un rango a, ..., b
    
    Parameters
    ----------
    a: int
        cota inferior a evaluar
    b: int
        cota superior a evaluar
    
    Returns
    -------
    list:
        elementos entre a, ... ,b que sean número de Amstrong
    """
    amstrong_numbers = []
    for i in range(a, b + 1):
        if is_amstrong(a):
            amstrong_numbers.append(i)
    
    return amstrong_numbers

if __name__ == "__main__":
    import sys
    # sys.argv es una lista de Python que contiene los argumentos
    # que se le pasaron a un script de python
    if len(sys.argv) > 1:
        number = sys.argv[1]
        val = "" if is_amstrong(number) else " no"
        print(f"{number}{val} es número de amstrong")
