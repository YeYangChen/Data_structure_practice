from Linked_List import Linked_List

class Poly_Val:
	def __init__(self, coef, exp):
		self.__coefficient = coef
		self.__exponent = exp
	def get_coefficient(self):
		return self.__coefficient
	def get_exponent(self):
		return self.__exponent
	def __str__(self):
		return str(self.__coefficient) + 'x^' + str(self.__exponent)

if __name__ == '__main__':
	p1 = Linked_List()
	p2 = Linked_List()
	p2.append_element(Poly_Val(3,1990))
	p2.append_element(Poly_Val(-2,14))
	p2.append_element(Poly_Val(11,1))
	p2.append_element(Poly_Val(5,0))
	p3 = Linked_List()
	p1_node = p1.header.next
	p2_node = p2.header.next
	while p1_node is not None or p2_node is not None:

		if p2_node is None and p1_node is not None:
			p3.append_element(Poly_Val(p1_node.get_coefficient(), p1_node.get_exponent()))
		elif p2_node is not None and p1_node is None:
			p3.append_element(Poly_Val(p2_node.get_coefficient(), p2_node.get_exponent()))
		elif p1_node.get_exponent() > p2_node.get_exponent():
			p3.append_element(Poly_Val(p1_node.get_coefficient(), p1_node.get_exponent()))
			p1_node = p1_node.next
		elif p1_node.get_exponent() < p2_node.get_exponent():
			p3.append_element(Poly_Val(p2_node.get_coefficient(), p2_node.get_exponent()))
			p2_node = p2_node.next 
		else:
			p3.append_element(Poly_Val(p2_node.get_coefficient()+p1_node.get_coefficient(), p1_node.get_exponent()))
			p1_node = p1_node.next 
			p2_node = p2_node.next
	print(p1)
	print(p2)
	print(p3)
 # our solution to build p3 is 22 lines of code