def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) != len(ids) or len(ids) != len(points):
            raise ValueError("All input lists must have the same length when strct is True.")
    else:
        min_length = min(len(names), len(ids), len(points))
        
        names = names[:min_length]
        ids = ids[:min_length]
        points = points[:min_length]

    zipped_result = list(zip(names, ids, points))
    
    return zipped_result

names = ["Alice", "Bob", "Charlie"]
ids = [101, 102, 103]
points = [1000, 1500, 1200]


print(my_zip(names, ids, points, strct=True))

names2 = ["Dave", "Eve"]
print(my_zip(names2, ids, points,strct=False))