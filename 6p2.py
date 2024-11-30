def my_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if key == 0:  #
                if data[j][0] > data[j + 1][0]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 1: 
                if data[j][1] > data[j + 1][1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 2: 
                if data[j][2] > data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

data = [
    ('Alice', 2, 5),
    ('Bob', 1, 10),
    ('Charlie', 3, 7)
]

sorted_by_name = my_sort(data, 0)
print("Sorted by name:", sorted_by_name)

sorted_by_id = my_sort(data, 1)
print("Sorted by Customer ID:", sorted_by_id)

sorted_by_points = my_sort(data, 2)
print("Sorted by shopping points:", sorted_by_points)