filo = input()
tipo = input()
classe = input()
#vertebrados
if filo == 'vertebrado':

    #Para AVE
    if tipo == 'ave':

        if classe == 'carnivoro':
            print('aguia')
        elif classe == 'onivoro':
            print('pomba')

    #Para MAMIFERO
    elif tipo == 'mamifero':

        if classe == 'onivoro':
            print('homem')
        elif classe == 'herbivoro':
            print('vaca')

#invertebrados
elif filo == 'invertebrado':

    #Para INSETO
    if tipo == 'inseto':

        if classe == 'hematofago':
            print('pulga')
        elif classe == 'herbivoro':
            print('lagarta')

    #Para ANELIDEO
    if tipo == 'anelideo':

        if classe == 'hematofago':
            print('sanguessuga')
        elif classe == 'onivoro':
            print('minhoca')
