# Condicionales con operadores and y or

usuario_logueado = False
usuario_admin  = True

if usuario_logueado and usuario_admin:
    print('Estas logueado y sos admin')
elif usuario_logueado:
    print('estas logueado como un  simple mortal')
else:
    print('sali de aca ')


if usuario_logueado or usuario_admin:
    print('Estas logueado y sos admin')
elif usuario_logueado:
    print('estas logueado solamente cmo un mortal')
else:
    print('sali de aca ')