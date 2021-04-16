from Sistema_lanchonete import Pizza
from Sistema_lanchonete import Lanche
from Sistema_lanchonete import Hamburguer
from Sistema_lanchonete import Pedido
import time


def cardapio():
	 pizza= [ "Havaiana", "Carne-de-Sol","Queijo","Frango"]
	 lanche = ["Pastel","Risolho","Joelho","Lasanha"]
	 hamburguer = ["Cheddar", "Big Mac", "Chicago Burguer", "Vegano"]
	 total = [ ]
	 itens = [ ]
	 print(""" 
			-  - - RESTAURANTE QUASE TRÊS LANCHES - - -
					
				  ______Cardápio_____
					
				  [ 1 ] -  Pizzas
				  [ 2 ] -  Lanches
				  [ 3 ] - Hámburguer
				  [ 4 ] - Encerrar Pedido""")
	 print("..."*34,"\n")
	 nome_cliente = str(input(" - - - > Qual o nome do Senhor(a)?: "))
	 while True:
	 	opcao =" "
	 	pedido= [1,2,3,4]
	 	Pedidos_restaurante = Pedido()
	 	while opcao not in pedido:
	 		opcao = int(input("\n  • Faça seu pedido: "))
	 		if opcao == 1:
	 			restaurante = Pizza()
	 			restaurante.sabores_pizza()
	 			escolha= int(input("\n  • Qual Sabor de sua preferência: "))
	 			if escolha == 1:
	 				restaurante.dados_pizza(pizza[0], 25.00, 1, 1200)
	 				total.append(pizza[0])
	 				itens.append(25.00)
	 				conta = sum(itens)
	 			elif escolha == 2:
	 				restaurante.dados_pizza(pizza[1], 28.00, 1, 1300)
	 				total.append(pizza[1])
	 				itens.append(28.00)
	 				conta = sum(itens)
	 			elif escolha == 3:
	 				restaurante.dados_pizza(pizza[2], 27.50, 1, 1000)
	 				total.append(pizza[2])
	 				itens.append(27.50)
	 				conta = sum(itens)
	 			else:
	 				escolha == 4
	 				restaurante.dados_pizza(pizza[3], 30.00, 1, 1400)
	 				total.append(pizza[3])
	 				itens.append(30.00)
	 				conta = sum(itens)		
	 		elif opcao == 2:
	 			restaurante = Lanche()
	 			restaurante.tipos_de_lanches()
	 			escolha= int(input("\n  • Qual Sabor de sua preferência: "))
	 			if escolha == 1:
	 				restaurante.dados_lanches(lanche[0], 1.5, 1, 150)
	 				total.append(lanche[0])
	 				itens.append(1.5)
	 				conta = sum(itens)
	 			elif escolha == 2:
	 				restaurante.dados_lanches(lanche[1], 3.00, 1, 200)
	 				total.append(lanche[1])
	 				itens.append(3.00)
	 				conta = sum(itens)
	 			elif escolha == 3:
	 				restaurante.dados_lanches(lanche[2], 2.50, 1, 180)
	 				total.append(lanche[2])
	 				itens.append(2.50)
	 				conta = sum(itens)
	 			else:
	 				escolha == 4
	 				restaurante.dados_lanches(lanche[3], 30.00, 1, 1_200)
	 				total.append(lanche[3])
	 				itens.append(30.00)
	 				conta = sum(itens)
	 		elif opcao == 3:
	 			restaurante = Hamburguer()
	 			restaurante.tipos_de_hambuguers()
	 			escolha= int(input("\n  • Qual Sabor de sua preferência: "))
	 			if escolha == 1:
	 				restaurante.dados_hamburguer(hamburguer[0], 11.50, 1, 500)
	 				total.append(hamburguer[0])
	 				itens.append(11.50)
	 				conta = sum(itens)
	 			elif escolha == 2:
	 				restaurante.dados_hamburguer(hamburguer[1], 12.50, 1, 600)
	 				total.append(hamburguer[1])
	 				itens.append(12.50)
	 				conta = sum(itens)
	 			elif escolha == 3:
	 				restaurante.dados_hamburguer(hamburguer[2], 14.50, 1, 700)
	 				total.append(hamburguer[2])
	 				itens.append(14.50)
	 				conta = sum(itens)
	 			else:
	 				escolha == 4
	 				restaurante.dados_hamburguer(hamburguer[3], 10.00, 1, 600)		
	 				total.append(hamburguer[3])
	 				itens.append(10.00)
	 				conta = sum(itens)
	 	if opcao == 4:
	 			troco_cliente = float(input("\n  • Quantia Paga pelo Serviço: "))
	 			print("..."*15,"\n")
	 			print("			 ..... Gerando Nota Fiscal .....\n")
	 			time.sleep(1.0)
	 			Pedidos_restaurante.comanda(nome_cliente, conta, total, troco_cliente )
	 			break
	  					
cardapio()
