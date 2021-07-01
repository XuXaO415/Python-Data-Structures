def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
        
        https://docs.python.org/3/library/functions.html
        isinstance()
    """
    
    for items in lst:
        if not isinstance(items, list):
            return False
    return True
     
print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))   