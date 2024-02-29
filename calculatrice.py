print('calculatrice complete')
nombre1=int(input('entre le nombre1:\n'))
operateur=input('entre l\'operateur:\n')
nombre2=int(input('entre le nombre2:\n'))
resultat=0
if operateur=='+':
    resultat=nombre1+nombre2
    print(f'somme de {nombre1} {nombre2} est le {resultat}')
elif operateur=='*':
      resultat=nombre1*nombre2
      print(f'produit de {nombre1} {nombre2 }est le {resultat}')
elif operateur=='-':
     resultat=nombre1-nombre2
     print(f'soustraction de {nombre1} {nombre2 }est le {resultat}')
elif operateur=='/':
     nombre2==0
     print(f'division par 0 n\'existe pas')
else:
     print(f'division de {nombre1} {nombre2 }est le {resultat}')
     
   
      