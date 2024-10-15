def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    iterations = 0
    upper_bound = None
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (iterations, arr[mid]) 
 
    # якщо елемент не знайдений
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
x = 4.0
result = binary_search(arr, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")

