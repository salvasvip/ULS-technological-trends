def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    #print(poblacion_paises['Bolivia'])
    print('----------------------------')
    for pais in poblacion_paises.keys():
        print(pais)
    print('----------------------------')
    for pais in poblacion_paises.values():
        print(pais)
    print('----------------------------')
    for pais in poblacion_paises.items():
        print(pais)
    print('----------------------------')
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')
    print('----------------------------')

if __name__ == '__main__':
    run()
