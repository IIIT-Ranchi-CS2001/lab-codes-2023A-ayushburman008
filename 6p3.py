def my_max(*args):
    if not args:
        return None  

    max_value = args[0]

    for num in args:
        if num > max_value:
            max_value = num  

    return max_value


print(my_max(1, 2, 3, 4, 5))                
print(my_max(*{5, 1, 2, 3, 4}))           
print(my_max(*(1, 2, 3, 4, 5)))