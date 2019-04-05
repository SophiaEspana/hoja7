print("Hoja # 6 Sophia España")
opcion = input('Elegir ejercicio: ') 

if opcion == '2A':
    A = [1,2,3,4]
    B = [5,6,7,8]
    C= [A* B  for A,B in zip (A,B)]
    print (A)
    print(B)
    print( C) 

if opcion == '2B':
    A = [1,2,3,4]
    B = [5,6,7,8]
    C= [[A,B]  for A,B in zip (A,B)]
    print(A)
    print(B)
    print(C) 

if opcion == '3':
    string = input("ingrese una palabra: ")
    dic=dict([(letter,string.count(letter))for letter in string[:-1]])
    print (dic)


if opcion == '4':
    import re
    def multiwordReplace(texto, diccionariopalabras):
        rc = re.compile('|'.join(map(re.escape, diccionariopalabras)))
        def cambio(palabra):
            return diccionariopalabras[palabra.group(0)]
        return rc.sub(cambio, texto)
    string1 = """Hola cerote, espero que estes muy bien. Ayer me recorde de la puta que vimos en el parque, me sentí estupido de querer bajarla 
    del arbol. Solo de pensarlo me comence a reir puro idiota en la oficina, pasar el tiempo contigo es la mera verga.""" 
    
    print (string1)

    diccionariopalabras = {'cerote': 'amigo','puta': 'fruta','estupido': 'tonto','idiota': 'loco','verga': 'diversion'}
    string2 = multiwordReplace(string1, diccionariopalabras)
    print (string2)


if opcion == '5':
    import math

    print ('David')
    print ('Sophia')
    print ('Leslie')
    print ('Denisse')
    print ('Boris')

    estudiante = input('Elegir Estudiante: ') 

    
    if estudiante == 'David':
        matematica= 64 
        circuitos = 94
        fisica = 82
        programacion = 91
        promedio = (matematica+circuitos+fisica+programacion)/4

        print ('matematica:',matematica,'circuitos:',circuitos,'fisica:',fisica,'programacion:',programacion,'promedio:',promedio)
        if (matematica >= circuitos or matematica >= fisica or matematica >= programacion):
            print ('nota mas alta matematica:',matematica)

        elif (circuitos >= matematica or circuitos >= fisica or circuitos >= programacion):
            print ('nota mas alta circuitos:',circuitos)

        elif (fisica >= circuitos or fisica >= matematica or fisica >= programacion):
            print ('nota mas alta fisica:',fisica)
    
        else: 
            print ('nota mas alta programacion', programacion)


    if estudiante == 'Sophia':
        matematica= 90 
        circuitos = 89
        fisica = 83
        programacion = 88
        promedio = (matematica+circuitos+fisica+programacion)/4
        print ('matematica:',matematica,'circuitos:',circuitos,'fisica:',fisica,'programacion:',programacion,'promedio:',promedio)
        if (matematica >= circuitos or matematica >= fisica or matematica >= programacion):
            print ('nota mas alta matematica:',matematica)

        elif (circuitos >= matematica or circuitos >= fisica or circuitos >= programacion):
            print ('nota mas alta circuitos:',circuitos)

        elif (fisica >= circuitos or fisica >= matematica or fisica >= programacion):
            print ('nota mas alta fisica:',fisica)
    
        else: 
            print ('nota mas alta programacion', programacion)

    if estudiante == 'Leslie':
        matematica= 98 
        circuitos = 89
        fisica = 80
        programacion = 70
        promedio = (matematica+circuitos+fisica+programacion)/4
        print ('matematica:',matematica,'circuitos:',circuitos,'fisica:',fisica,'programacion:',programacion,'promedio:',promedio)
        if (matematica >= circuitos or matematica >= fisica or matematica >= programacion):
            print ('nota mas alta matematica:',matematica)

        elif (circuitos >= matematica or circuitos >= fisica or circuitos >= programacion):
            print ('nota mas alta circuitos:',circuitos)

        elif (fisica >= circuitos or fisica >= matematica or fisica >= programacion):
            print ('nota mas alta fisica:',fisica)
    
        else: 
            print ('nota mas alta programacion', programacion)

    if estudiante == 'Denisse':
        matematica= 64
        circuitos = 69
        fisica = 90
        programacion = 80
        promedio = (matematica+circuitos+fisica+programacion)/4
        print ('matematica:',matematica,'circuitos:',circuitos,'fisica:',fisica,'programacion:',programacion,'promedio:',promedio)

        if (matematica >= circuitos or matematica >= fisica or matematica >= programacion):
            print ('nota mas alta matematica:',matematica)

        elif (circuitos >= matematica or circuitos >= fisica or circuitos >= programacion):
            print ('nota mas alta circuitos:',circuitos)

        elif (fisica >= circuitos or fisica >= matematica or fisica >= programacion):
            print ('nota mas alta fisica:',fisica)
    
        else: 
            print ('nota mas alta programacion', programacion)


    if estudiante == 'Boris':
        matematica= 80 
        circuitos = 66
        fisica = 76
        programacion = 89
        promedio = (matematica+circuitos+fisica+programacion)/4
        print ('matematica:',matematica,'circuitos:',circuitos,'fisica:',fisica,'programacion:',programacion, 'promedio:',promedio)
    
        if (matematica >= circuitos or matematica >= fisica or matematica >= programacion):
            print ('nota mas alta matematica:',matematica)

        elif (circuitos >= matematica or circuitos >= fisica or circuitos >= programacion):
            print ('nota mas alta circuitos:',circuitos)

        elif (fisica >= circuitos or fisica >= matematica or fisica >= programacion):
            print ('nota mas alta fisica:',fisica)
    
        else: 
            print ('nota mas alta programacion', programacion)


