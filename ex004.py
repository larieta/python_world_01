n = (input('type something: '))

print(f'''Primitive type? {type(n)} 
Is it only made by spaces? {n.isspace() }
Is it numeric? {n.isnumeric()} 
Is it alphabetic? {n.isalpha()} 
Is it alphanumeric? {n.isalnum()} 
Is it uppercase? {n.isupper()} 
Is it lowercase? {n.islower()}''')