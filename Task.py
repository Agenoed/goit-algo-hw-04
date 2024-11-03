import timeit
import random

def merge_sort(arr):
    """
    Сортування злиттям.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    """
    Сортування вставками.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    """
    Timsort (вбудована функція sorted()).
    """
    return sorted(arr)

# Створення наборів даних для тестування:
data_random = [random.randint(0, 1000) for _ in range(1000)]
data_sorted = sorted(data_random)
data_reverse_sorted = sorted(data_random, reverse=True)
data_few_unique = [random.randint(0, 10) for _ in range(1000)]

# Тестування алгоритмів на різних наборах даних
def test_sort(data, sort_func, name):
  time_taken = timeit.timeit(lambda: sort_func(data.copy()), number=100)
  print(f"Час виконання {name}: {time_taken:.6f} секунд")

test_sort(data_random, merge_sort, "Сортування злиттям (випадкові дані)")
test_sort(data_sorted, merge_sort, "Сортування злиттям (відсортовані дані)")
test_sort(data_reverse_sorted, merge_sort, "Сортування злиттям (зворотньо відсортовані дані)")
test_sort(data_few_unique, merge_sort, "Сортування злиттям (дані з невеликою кількістю унікальних елементів)")

test_sort(data_random, insertion_sort, "Сортування вставками (випадкові дані)")
test_sort(data_sorted, insertion_sort, "Сортування вставками (відсортовані дані)")
test_sort(data_reverse_sorted, insertion_sort, "Сортування вставками (зворотньо відсортовані дані)")
test_sort(data_few_unique, insertion_sort, "Сортування вставками (дані з невеликою кількістю унікальних елементів)")

test_sort(data_random, timsort, "Timsort (випадкові дані)")
test_sort(data_sorted, timsort, "Timsort (відсортовані дані)")
test_sort(data_reverse_sorted, timsort, "Timsort (зворотньо відсортовані дані)")
test_sort(data_few_unique, timsort, "Timsort (дані з невеликою кількістю унікальних елементів)")