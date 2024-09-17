import Pyro4
@Pyro4.expose 


class Warehouse():
    def __init__(self, c):
        self.contents = c
        
    def list_contents(self):
        return self.contents

    def take(self, name, item):
        self.contents.remove(item)
        print(name, " retirou ", item)

    def store(self, name, item):
        self.contents.append(item)
        print(name, " armazenou ", item)
        print(self.contents)

def main():
    minhaWare = Warehouse({"cadeira","bike","lâmpada"})
    Pyro4.Daemon.serveSimple(
        {
            minhaWare: "example.warehouse"
        }
    )
    
if __name__ =="__main__":
    main()
