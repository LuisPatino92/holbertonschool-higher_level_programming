def uniq_add(my_list=[]):
    added = []
    suma = 0
    for element in my_list:
        if element not in added:
            suma += element
            added += [element]
    return suma
