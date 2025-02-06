from ordered_list import get_ordered_list

def search_ordered_list(lst, target):
 
    sorted_list = get_ordered_list(lst)
    
 
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return True  
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False  