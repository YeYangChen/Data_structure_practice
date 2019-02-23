from Linked_List import Linked_List

def intersection(a, b):
	c = Linked_List()
	index_a = 0; index_b = 0
	while index_a < a.size and index_b < b.size:
		if a.get_element_at(index_a) < b.get_element_at(index_b):
			index_a = index_a + 1
		elif a.get_element_at(index_a) > b.get_element_at(index_b):
			index_b = index_b + 1
		else:
			c.append_element(a.get_element_at(index_a))
			index_a = index_a + 1
			index_b = index_b + 1
	return c

def lastIndexOf(self, val):
	index = -1
	current = self.head.next
	for k in range(self.size):
		if current.element == val:
			index = k
		current = current.next
	if index < 0:
		return
	else:
		return index

def __len__(self):
	if self.enter is None:
		return 0
	count = 1
	current = self.enter
	while current.next is not self.enter:
		count = count + 1
		current = current.next
	return count

def next_to_last(self):
	#return get_element_at(self.size - 1)
	if self.size < 2:
		return none
	return self.trailer.prev.prev.element

def swap(a, b):
	temp = a.next
	a.next = b.next
	b.next = temp
	temp = a.prev
	a.prev = b.prev
	b.prev = temp
