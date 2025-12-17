import pytest
import my_math_lib


class TestFibonacciNumbers:
    def test_fibonacci_positive(self):
        # Тест на корректных данных: n > 0
        assert my_math_lib.fibonacci_numbers(5) == [0, 1, 1, 2, 3]
        assert my_math_lib.fibonacci_numbers(7) == [0, 1, 1, 2, 3, 5, 8]
    def test_fibonacci_boundary_small(self):
        # Тест граничных значений: n = 0, 1, 2
        assert my_math_lib.fibonacci_numbers(0) == []
        assert my_math_lib.fibonacci_numbers(1) == [0]
        assert my_math_lib.fibonacci_numbers(2) == [0, 1]
    def test_fibonacci_negative_n(self):
        # Тест на некорректных данных: n < 0
        with pytest.raises(ValueError, match="n должно быть неотрицательным числом"):
            my_math_lib.fibonacci_numbers(-1)
        with pytest.raises(ValueError, match="n должно быть неотрицательным числом"):
            my_math_lib.fibonacci_numbers(-10)
    def test_fibonacci_large_n(self):
        # Тест на большом n (проверка производительности)
        # Граничное значение: большое n
        result = my_math_lib.fibonacci_numbers(10)
        assert len(result) == 10
        assert result[:5] == [0, 1, 1, 2, 3]
        # Проверяем свойство чисел Фибоначчи
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]

class TestBubbleSort:
    def test_bubble_sort_correct(self):
        # Тест на корректных данных: различные списки
        assert my_math_lib.bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert my_math_lib.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert my_math_lib.bubble_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]
    def test_bubble_sort_boundary(self):
        # Тест граничных значений
        assert my_math_lib.bubble_sort([]) == []
        assert my_math_lib.bubble_sort([42]) == [42]
        assert my_math_lib.bubble_sort([-5, 0, 5, -10]) == [-10, -5, 0, 5]
    def test_bubble_sort_duplicates(self):
        # Тест списка с повторяющимися значениями
        assert my_math_lib.bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]
        assert my_math_lib.bubble_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
    def test_bubble_sort_invalid_input(self):
        # Тест на некорректных данных
        with pytest.raises(TypeError, match="Входной аргумент должен быть списком"):
            my_math_lib.bubble_sort("не список")
        with pytest.raises(TypeError, match="Входной аргумент должен быть списком"):
            my_math_lib.bubble_sort(123)
    def test_bubble_sort_original_unchanged(self):
        # Тест, что исходный список не изменяется
        original = [3, 1, 4, 2]
        sorted_list = my_math_lib.bubble_sort(original)
        assert original == [3, 1, 4, 2]  # Исходный не изменился
        assert sorted_list == [1, 2, 3, 4]  # Копия отсортирована

class TestEratosthenesSieve:
    def test_eratosthenes_correct(self):
        # Тест на корректных данных: n > 2
        assert my_math_lib.eratosthenes_sieve(10) == [2, 3, 5, 7]
        assert my_math_lib.eratosthenes_sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    def test_eratosthenes_boundary_small(self):
        # Тест граничных значений: n <= 2
        assert my_math_lib.eratosthenes_sieve(0) == []
        assert my_math_lib.eratosthenes_sieve(1) == []
        assert my_math_lib.eratosthenes_sieve(2) == []
        assert my_math_lib.eratosthenes_sieve(3) == [2]
    def test_eratosthenes_negative_n(self):
        # Тест на некорректных данных: n < 0
        with pytest.raises(ValueError, match="n должно быть неотрицательным числом"):
            my_math_lib.eratosthenes_sieve(-5)
    def test_eratosthenes_large_n(self):
        # Тест на большом n (проверка корректности алгоритма)
        primes = my_math_lib.eratosthenes_sieve(100)
        assert primes[:10] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert len(primes) == 25
        # Проверяем, что все числа в списке действительно простые
        for p in primes:
            for i in range(2, int(p**0.5) + 1):
                assert p % i != 0, f"{p} не является простым числом"
    def test_eratosthenes_property(self):
        # Тест свойства простых чисел: нет делителей кроме 1 и самого себя
        primes = my_math_lib.eratosthenes_sieve(50)
        for prime in primes:
            divisors = 0
            for i in range(2, int(prime**0.5) + 1):
                if prime % i == 0:
                    divisors += 1
            assert divisors == 0, f"Число {prime} не является простым"
