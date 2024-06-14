def factorial(natural):
    if natural == 0:
        retorno =  1
    else:
        retorno = natural * factorial(natural - 1)
    
    return retorno 