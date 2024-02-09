balance = 500

if balance < 499:
    print('Sos pobre gato')
else:
    print('Gato')

# IF la condicion se cumple la negamos con not
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Good Choice!')

# IF boolean

usuarios_activos = False
usuarios_admin = True
if usuarios_activos: 
    if usuarios_admin:
        print('Todo Bien con vos, hiciste lo que debias hacer')
    else:
        print('No Sos activo pa, pa fuera.')
else:
    print('no estas logueado pa, anda loguearte')