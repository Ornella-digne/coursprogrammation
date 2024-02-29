nonbre=int(input('entre le nombre:\n'))
action =input('entre l\'action:\n')
if action=='carre':
   resultat=nombre*nombre
   print(f'le carre de {nombre} {nombre} est le {resultat}')
elif action=='cube':
     resultat=nombre*nombre*nombre
     print(f'le cube de {nombre} {nombre} est le {resultat}')
else:
    print(f'l\'action n\'existe pas')