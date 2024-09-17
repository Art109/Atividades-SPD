class Person():
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("Aqui eh ", self.name)
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Obrigada e volte sempre!")

    def deposit(self, warehouse ):
        print("-" * 32, "\nO armazem contém: ", warehouse.list_contents())
        item = input("Entre com o item que deseja inserir (ou deixe em branco)")
        if item:
            warehouse.store(self.name, item)
        print("O armazem agora contém: ", warehouse.list_contents())

    def retrieve(self, warehouse):
        print("-" * 32, "\nO armazem contém: ", warehouse.list_contents())
        item = input("Entre com o item que deseja retirar (ou deixe em branco)")
        if item:
            warehouse.take(self.name, item)
        print("O armazem agora contém: ", warehouse.list_contents())

