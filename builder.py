from abc import ABC, abstractmethod


atendimento = int(input("Olá \n 1. Monte seu Lanche\n 2. Escolha seu Lanche Pronto"))

if atendimento == 1:
    class burguer :
        def __init__(self):
            self.bread = None
            self.cheese = None
            self.meat = None
            self.vegetables = None
            self.sauce = None

        
        def __str__(self):
            return f"\nSeu pedido é:\nPão: {self.bread}\nCarne: {self.meat}\nQueijo: {self.cheese}\nVegetais: {self.vegetables}\nMolho: {self.sauce}"



    class BurguerBuilder:
        def __init__(self) -> None:
            self.burguer = burguer()

        def add_bread(self):
            escolha = int(input("Escolha a opção \n 1. Parmesão \n 2. 9 Grãos \n 3. Italiano \n"))
            if escolha == 1:
                self.burguer.bread = "Parmesão"
            elif escolha == 2:
                self.burguer.bread = "9 Grãos"
            elif escolha == 3:
                self.burguer.bread = "Italiano"
            else: 
                print("Opção Invalida")


        def add_meat(self):
            escolha = int(input("Escolha a opção \n 1. Carne \n 2. Frango \n 3. Linguiça \n 4. Vegetariano \n"))
            if escolha == 1:
                self.burguer.meat = "Carne"
            elif escolha == 2:
                self.burguer.meat= "Frango"
            elif escolha == 3:
                self.burguer.meat = "Linguiça "
            elif escolha == 4:
                self.burguer.meat = "Vegetariano"
            else: 
                print("Opção Invalida")




        def add_cheese(self):
            escolha = int(input("Escolha a opção \n 1. cheddar\n 2. suíço \n 3. muçarela \n"))
            if escolha == 1:
                self.burguer.cheese = "cheddar,"
            elif escolha == 2:
                self.burguer.cheese = "suíço"
            elif escolha == 3:
                self.burguer.cheese = "muçarela"
            else: 
                print("Opção Invalida")



        def add_vegetables(self):
            escolha = int(input("Escolha a opção \n 1. azeitona \n 2. alface \n 3. tomate\n "))
            if escolha == 1:
                self.burguer.vegetables = "azeitona"
            elif escolha == 2:
                self.burguer.vegetables = "alface"
            elif escolha == 3:
                self.burguer.vegetables = "tomate"
            else: 
                print("\nOpção Invalida \n")

        



        def add_sauce(self):
            escolha = int(input("Escolha a opção \n 1. Barbecue \n 2. Chipotle \n 3. Supreme \n"))
            if escolha == 1:
                self.burguer.sauce = "Barbecue"
            elif escolha == 2:
                self.burguer.sauce = "Chipotle"
            elif escolha == 3:
                self.burguer.sauce = "Supreme"
            else: 
                print("Opção Invalida")




        def get_burguer(self):
            return self.burguer


    class Director:
        def __init__(self, builder):
            self.builder = builder

        

        def construct_burguer(self):
            self.builder.add_meat()
            self.builder.add_bread()
            self.builder.add_vegetables()
            self.builder.add_cheese()
            self.builder.add_sauce()




    burguer = BurguerBuilder()
    diretor = Director(burguer)
    diretor.construct_burguer() 
    lanche = burguer.get_burguer()
    print(lanche)












#====================== LANCHES PRONTOS =====================================
elif atendimento == 2 :

    class AbstractProductA(ABC):
        @abstractmethod
        def operation_a(self) -> str:
            pass


    #Classes concretas de produtos A1 e A2
    class Frango(AbstractProductA):
        def operation_a(self) -> str:
            return "Frango"

    class Vegetariano(AbstractProductA):
        def operation_a(self) -> str:
            return "Vegetariano"
        

    class Carne_Supreme(AbstractProductA):
        def operation_a(self) -> str:
            return "Carne_Supreme"

    class BMT(AbstractProductA):
        def operation_a(self) -> str:
            return "BMT"
        

    class Frango_Empanado(AbstractProductA):
        def operation_a(self) -> str:
            return "Frango_Empanado"



    #Classes concretas de produtos B1 e B2


    # Interface abstrata da fábrica abstrata
    class AbstractFactory(ABC):
        @abstractmethod
        def create_product_a(self) -> AbstractProductA:
            pass
        

    # Classes concretas da fábrica abstrata
    class Frango(AbstractFactory):
        def create_product_a(self) -> AbstractProductA:
            return Frango()


    class Carne_Supreme_Factory(AbstractFactory):
        def create_product_a(self) -> AbstractProductA:
            return Carne_Supreme()

    class BMT_Factory(AbstractFactory):
        def create_product_a(self) -> AbstractProductA:
            return BMT()
        

    class Frango_Empanado_Factory(AbstractFactory):
        def create_product_a(self) -> AbstractProductA:
            return Frango_Empanado()




    # Cliente
    class Client:
        def __init__(self, factory: AbstractFactory) -> None:
            self._product_a = factory.create_product_a()
            
        
        def run(self) -> None:
            print(self._product_a.operation_a())


    escolha = int(input("Opção do Cardapio \n 1. Frango \n 2. Carne Supreme \n 3. BMT \n 4.Frango Empanado  "))
    if  escolha == 1 :
        print("Sua Escolha foi: ")
        client1 = Client(Frango())
        client1.run()

    elif escolha == 2 :
        print("Sua Escolha foi: ")
        client1 = Client(Carne_Supreme_Factory())
        client1.run()
        
    elif escolha == 3 :
        print("Sua Escolha foi: ")
        client1 = Client(BMT_Factory())
        client1.run()

    elif escolha == 4 :
        print("Sua Escolha foi: ")
        client1 = Client(Frango_Empanado_Factory())
        client1.run()



