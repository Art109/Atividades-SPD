import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:9050')

print(s.potencia(2,3))
print(s.soma(3, 5))
