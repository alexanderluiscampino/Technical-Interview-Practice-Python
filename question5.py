class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None



def question5(ll, m):
	# Setting up initial values - head of linked list
	p1 = ll
	p2 = ll

	# This cycle sets p1 m positions in front of p2
	for i in range(0, m):
		if (p1 == None):
			return None
		p1 = p1.next
	# This while loop will run until p1 get to the last element of list
	# at the time p2 will be m positions behin
	# p2 value is returned, since that with be the mth element
	# in the linked list
	while (p1 != None):
		p1 = p1.next
		p2 = p2.next
	return p2.data


A = Node(2)
B = Node(3)
C = Node(8)
D = Node(1)
E = Node(6)

A.next = B
B.next = C
C.next = D
D.next = E

print(question5(A, 3))
