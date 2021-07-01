def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    
    return phrase.title()

print(capitalize('python'))
print(capitalize('only first word')) 
