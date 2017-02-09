            
def find_missing(array1,array2):
    if array1 == [] or array2 == [] or array1 == array2:
        return 0
    for x in array1:
        if x not in array2:
            return x
    for y in array2:
        if y not in array1:
            return y