'''Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x ∈ R (x dado en radianes), utilizando los primeros n términos de la serie de Maclaurin'''

def aproxCos(x,n):
  s = 0
  for i in range(0,n+1):
    factorial = 1
    for j in range(1, (2*i)+1):
      factorial = factorial*j
    #print('Factorial de ' + str(i) + ' = ' + str(factorial))
    s += ( ( (-1)**i ) * ( x**(2*i) )) /factorial
    #print('Denominador = ' + str(( ( (-1)**i ) * ( x**(2*i + 1 ) ))))
  return s

print(str(aproxCos(0,20)))