tree = ['dog', ['raccoon','bear'], [['sea_lion','seal'],['monkey','cat'], 'weasel']]

def contains(my_list, target): 
    result = False 
    for element in my_list: 
        if isinstance(element, list): 
            if contains(element, target): 
                result = True 
        else: 
            if element == target: 
                result = True 
    return result 

def are_closely_related(my_list, taxon1, taxon2, taxon3): 
    result = False 
    if (contains(my_list, taxon1) and contains(my_list, taxon2) 
    and not contains(my_list, taxon3)): 
        result = True 
    for sublist in my_list: 
        if isinstance(sublist, list): 
            if are_closely_related(sublist, taxon1, taxon2, taxon3): 
                result = True 
    return result

# false case first, then 3 true cases
print are_closely_related(tree, 'man', 'woman', 'child') == True 
print are_closely_related(tree, 'raccoon', 'dog', 'bear') == False 
print are_closely_related(tree, 'raccoon', 'bear', 'weasel') == True 
print are_closely_related(tree, 'raccoon', 'bear', 'dog') == True
