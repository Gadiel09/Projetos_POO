import math
class Pizza:
		def sabores_pizza(self):
			print(""" 
			
			SABORES DE PIZZAS DISPONÍVEIS
			
	[ 1 ] - Havaiana
	[ 2 ] - Carne-de-Sol
	[ 3 ] - Queijo
	[ 4 ] - Frango
			""")
		
		
					
				
				
				
				
				
		def dados_pizza(self, nome, preco, validade, peso):
				self.nome = nome
				self.preco = preco
				self.validade = validade
				self.peso = peso
				if peso < 999:
				 	print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
				if peso >= 1000:
					 print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
								

class Pedido:
	def comanda(self, nome,preco,comidas, quantia):
		self.nome = nome
		self.preco = preco
		self.comidas = comidas
		self.quantia = quantia
		trouco = self.quantia - self.preco 
		if self.preco > trouco:
			print(f"  • Desculpe-nos Sr.{self.nome} o seu saldo é insuficiente !")
		else:
			print(f""" 
			
			(___ NOTA FISCAL ___)
			
		 Lanchonete Quase Três Lanches	
		
	---> Dono(a)_Pedido : {self.nome}
	---> Valor : R$ {self.preco}0 reais
	---> Valor Pago: R$ {self.quantia} reais
	---> Troco do Cliente : R$ {math.ceil(trouco)} reais
			""")
			print("		---> Pedidos: ") 
			print()
			for item in self.comidas:
				print(f" 		[ {item:^10} ]")	



class Lanche:
	def tipos_de_lanches(self):
		print(""" 
			
			LANCHES DISPONÍVEIS
			
	[ 1 ] - Pastel
	[ 2 ] - Risolho
	[ 3 ] - Joelho
	[ 4 ] - Lasanha
			""")		
			
			
	def dados_lanches(self, nome, preco, validade, peso):
				self.nome = nome
				self.preco = preco
				self.validade = validade
				self.peso = peso	
				if peso < 999:
				 	print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
				if peso >= 1000:
					 print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
				
	
				
				
				
				
			
class Hamburguer:
		def tipos_de_hambuguers(self):
			print(""" 
			
			HÁMBURGUES  DISPONÍVEIS
			
	[ 1 ] - Cheddar
	[ 2 ] - Big Mac
	[ 3 ] - Chicago Burguer
	[ 4 ] - Vegano
			""")		
			
			
		def dados_hamburguer(self, nome, preco, validade, peso):
				self.nome = nome
				self.preco = preco
				self.validade = validade
				self.peso = peso	
				if peso < 999:
				 	print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
				if peso >= 1000:
					 print ( f""" 
	— > Pizza: {self.nome}
	— > Valor: {self.preco}0 reais
	— > Valid: {self.validade}h
	— > Pesos: {self.peso} gramas
				""")
				
				
						
