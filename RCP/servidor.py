from xmlrpc.server import SimpleXMLRPCServer



server = SimpleXMLRPCServer(("localhost" , 9050))

def soma(a , b):
    return a + b

server.register_function(pow, 'potencia')

server.register_function(soma, 'soma')


server.register_introspection_functions()


server.serve_forever()


