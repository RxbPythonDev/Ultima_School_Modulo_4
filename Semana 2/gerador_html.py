import random

numero = random.randint(1,100)

html = f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>O numero: {numero}</h1>
  </body>
</html>  
'''

with open('numero.html', 'w') as arquivo:
    arquivo.write(html)

print('Gerou')
