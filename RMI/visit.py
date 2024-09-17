#from warehouse import Warehouse
from person import Person

#itens = ["cadeira", "bike", "lâmpada"]
#w = Warehouse(itens)

import Pyro4
uri = input("Entre com o uri do armazém")
w = Pyro4.Proxy(uri)

bianca = Person("Bianca")
fulano = Person("Fulano")

bianca.visit(w)
fulano.visit(w)
