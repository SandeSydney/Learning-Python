## Functions can take arguments that will be later used inside the function

def salimia(lugha):
        if lugha == 'es':
            return('Hola')
        elif lugha == 'fr':
            return('Bonjour')
        else:
            return('Hello')

print(salimia('en'), 'George')
print(salimia('fr'), 'Master')
print(salimia('es'), 'Calito')