from abc import ABC, abstractmethod
import time

def main():
    atendimento = int(input("Olá, seja bem vindo ao Subway da Fatec Diadema!\n\nDigite 1 para montar seu lanche\nDigite 2 para escolher um lanche pronto\n\nDigite sua opção: "))

    if atendimento == 1:
        class burguer :
            def __init__(self):
                self.bread = None
                self.cheese = None
                self.meat = None
                self.vegetables = None
                self.sauce = None

            
            def __str__(self):
                return f"\nSeu pedido é:\nPão: {self.bread}\nCarne: {self.meat}\nVegetais: {self.vegetables[0]}, {self.vegetables[1]} e {self.vegetables[2]}\nQueijo: {self.cheese}\nMolhos: {self.sauce[0]}, {self.sauce[1]} e {self.sauce[2]}"



        class BurguerBuilder:
            def __init__(self) -> None:
                self.burguer = burguer()

            def add_bread(self):
                escolha = int(input("\nEscolha um pão:\n - 1. Três Queijos \n - 2. Italiano Branco \n - 3. 9 Grãos\n - 4. Parmesão \n - 5. Orégano\n\nDigite sua opção: "))
                if escolha == 1:
                    self.burguer.bread = "Três Queijos"

                elif escolha == 2:
                    self.burguer.bread = "Italiano Branco"

                elif escolha == 3:
                    self.burguer.bread = "9 Grãos"

                elif escolha == 4:
                    self.burguer.bread = "Parmesão"

                elif escolha == 5:
                    self.burguer.bread = "Orégano"
                else: 
                    print("Opção inválida! Repita o pão.")
                    self.add_bread()


            def add_meat(self):
                escolha = int(input("\nEscolha a carne: \n 1. Carne \n 2. Frango \n 3. Vegetariano \n 4. Linguiça\n\nDigite sua opção: "))
                if escolha == 1:
                    self.burguer.meat = "Carne"

                elif escolha == 2:
                    self.burguer.meat = "Frango"

                elif escolha == 3:
                    self.burguer.meat = "Vegetariano"

                elif escolha == 4:
                    self.burguer.meat = "Linguiça"

                else: 
                    print("Opção inválida! Repita a carne.")
                    self.add_meat()

            def add_cheese(self):
                escolha = int(input("Escolha o queijo: \n 1. Cheddar\n 2. Suíço \n 3. Muçarela\n\nDigite sua opção: "))
                if escolha == 1:
                    self.burguer.cheese = "Cheddar"

                elif escolha == 2:
                    self.burguer.cheese = "Suíço"

                elif escolha == 3:
                    self.burguer.cheese = "Muçarela"

                else: 
                    print("Opção inválida")
                    self.add_cheese()

            def add_vegetables(self):
                veg = []
                while len(veg) < 3:
                    escolha = int(input("\nEscolha 3 vegetais! \nVegetais escolhidos: {0} \n 1. Alface \n 2. Cebola \n 3. Tomate \n 4. Cebola roxa \n 5. Pepino \n 6. Pimentão \n 7. Picles \n 8. Azeitona\n\nDigite sua opção: " .format(veg)))
                    if escolha == 1:
                        if "Alface" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Alface")

                    elif escolha == 2:
                        if "Cebola" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Cebola")

                    elif escolha == 3:
                        if "Tomate" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Tomate")

                    elif escolha == 4:
                        if "Cebola roxa" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Cebola roxa")

                    elif escolha == 5:
                        if "Pepino" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Pepino")

                    elif escolha == 6:
                        if "Pimentão" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Pimentão")

                    elif escolha == 7:
                        if "Picles" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Picles")

                    elif escolha == 8:
                        if "Azeitona" in veg:
                            print('\nVocê já escolheu isso! Escolha outro.')
                        else:
                            veg.append("Azeitona")

                    else: 
                        print("\nOpção inválida! Repita o vegetal.")

                self.burguer.vegetables = veg

            def add_sauce(self):
                sauce = []
                while len(sauce) < 3:
                    escolha = int(input("Escolha 3 molhos!\nMolhos escolhidos: {0}\n 1. Barbecue \n 2. Maionese \n 3. Maionese temperada\n 4. Mostarda e Mel\n 5. Cebola agridoce\n 6. Chipotle\n 7. Parmesão\n 8. Supreme\n\nDigite sua opção: " .format(sauce)))
                    if escolha == 1:
                        if "Barbecue" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Barbecue")

                    elif escolha == 2:
                        if "Maionese" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Maionese")

                    elif escolha == 3:
                        if "Maionese temperada" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Maionese temperada")
                    
                    elif escolha == 4:
                        if "Mostarda e Mel" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Mostarda e Mel")
                    
                    elif escolha == 5:
                        if "Cebola agridoce" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Cebola agridoce")
                        
                    elif escolha == 6:
                        if "Chipotle" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Chipotle")
                    
                    elif escolha == 7:
                        if "Parmesão" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Parmesão")
                    
                    elif escolha == 8:
                        if "Supreme" in sauce:
                            print('\nVocê já escolheu isso! Escolha outro.\n')
                        else:
                            sauce.append("Supreme")
                    else: 
                            print("\nOpção inválida! Repita o molho.\n")
                self.burguer.sauce = sauce

            def get_burguer(self):
                return self.burguer

        class Director:
            def __init__(self, builder):
                self.builder = builder

            def construct_burguer(self):
                self.builder.add_bread()
                self.builder.add_meat()
                self.builder.add_vegetables()
                self.builder.add_cheese()
                self.builder.add_sauce()

        burguer = BurguerBuilder()
        diretor = Director(burguer)
        diretor.construct_burguer() 
        lanche = burguer.get_burguer()
        print(lanche)

        print('\n\nMuito obrigado por vir ao Fatec Way!\n')
        voltar = int(input('\nDeseja pedir novamente? Caso sim, entre com o número 1 abaixo!\n'))
        if voltar == 1:
            print('\n')
            main()
        else:
            print('Volte sempre!\n\nSaindo 3...')
            time.sleep(1)
            print('2...')
            time.sleep(1)
            print('1...')
            time.sleep(1)
            exit()
        

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
            
        class Carne_Supreme(AbstractProductA):
            def operation_a(self) -> str:
                return "Carne Supreme"

        class BMT(AbstractProductA):
            def operation_a(self) -> str:
                return "BMT"
            
        class Frango_Empanado(AbstractProductA):
            def operation_a(self) -> str:
                return "Frango Empanado"
        
        class Vegetariano(AbstractProductA):
            def operation_a(self) -> str:
                return "Vegetariano"

        # Classes concretas de produtos B1 e B2

        # Interface abstrata da fábrica abstrata
        class AbstractFactory(ABC):
            @abstractmethod
            def create_product_a(self) -> AbstractProductA:
                pass

        # Classes concretas da fábrica abstrata
        class Frango_Factory(AbstractFactory):
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
        
        class  Vegetariano_Factory(AbstractFactory):
            def create_product_a(self) -> AbstractProductA:
                return Vegetariano()
            
        # Cliente
        class Client:
            def __init__(self, factory: AbstractFactory) -> None:
                self._product_a = factory.create_product_a()
            
            def run(self) -> None:
                print(self._product_a.operation_a())

        escolha = int(input("\nAqui estão as opções do nosso cardápio!\n\n 1. Frango\n 2. Carne Supreme\n 3. BMT\n 4. Frango Empanado\n 5. Vegetariano\n\n Digite qual desses você deseja: "))
        if  escolha == 1 :
            print("\nSua Escolha foi: ")
            client1 = Client(Frango_Factory())
            client1.run()

        elif escolha == 2 :
            print("\nSua Escolha foi: ")
            client1 = Client(Carne_Supreme_Factory())
            client1.run()
            
        elif escolha == 3 :
            print("\nSua Escolha foi: ")
            client1 = Client(BMT_Factory())
            client1.run()

        elif escolha == 4 :
            print("\nSua Escolha foi: ")
            client1 = Client(Frango_Empanado_Factory())
            client1.run()

        elif escolha == 5 :
            print("\nSua Escolha foi: ")
            client1 = Client(Vegetariano_Factory())
            client1.run()
        
        print('\n\nMuito obrigado por vir ao Fatec Way!\n')
        voltar = int(input('\nDeseja pedir novamente? Caso sim, entre com o número 1 abaixo!\n'))
        if voltar == 1:
            print('\n')
            main()
        else:
            print('Volte sempre!\n\nSaindo 3...')
            time.sleep(1)
            print('2...')
            time.sleep(1)
            print('1...')
            time.sleep(1)
            exit()


if __name__ == '__main__':
    main() 