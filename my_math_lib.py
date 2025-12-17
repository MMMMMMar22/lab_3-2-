def fibonacci_numbers(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным числом")
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Входной аргумент должен быть списком")
    
    # Создаем копию, чтобы не изменять исходный список
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
                swapped = True
        # Если не было обменов, список уже отсортирован
        if not swapped:
            break
    return sorted_arr

def eratosthenes_sieve(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным числом")
    
    if n <= 2:
        return []
    
    # Инициализация списка: True - число простое, False - составное
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Помечаем все кратные i как составные
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Формируем список простых чисел
    primes = [i for i in range(2, n) if is_prime[i]]
    return primes
