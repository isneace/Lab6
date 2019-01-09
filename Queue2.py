from QueueNode import Node

class Queue2:

	def __init__(self):
		self.head  = None
		self.front = None
		self.count = 0

	def getHead(self):
		return self.head

	def getFront(self):
		return self.front

	def isEmpty(self):
		return self.head == None

	def size(self):
		return self.count

	def enqueue(self, item):
		print "Enqueuing ..."
		temp      = Node(item)
		# Case 1: Queue is Empty:
		if self.head == None:
			temp.setNext(self.head)
			temp.setPrev(self.front)
			self.head = temp
			self.front = temp

		# Case 2: Queue is not Empty:
		else:
			current = self.head
			current.setPrev(temp)
			temp.setNext(self.head)
			self.head = temp

		self.count += 1 
		
		print "Queue Count= ", self.count
	


	def dequeue(self):
		current  = self.front

		if current == None:
			print "Queue is Empty !!!" 		
		
		elif self.count == 1:
	
			self.head  = None
			self.front = None
			self.count = 0
		else:
			print "Dequeuing item: ", current.getData()
 		
			self.front  = current.getPrev()
			previous    = current.getPrev()
			previous.setNext(None)
			self.count -= 1 
		
			print "Queue Count= ", self.count

		return current

	def index(self,item):
		current  = self.head
		position = 0
		found    = False

		print "Searching List for item", item
		while current != None:

			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", position
				found = True
				break

			current   = current.getNext()
			position += 1

		if not found:
			print "Item: ", item, "Was Not Found On List"
			position = -1

		return position

	def search(self,item):
		current = self.head
		count   = 0
		found   = False

		print "Searching List for item", item
		while current != None:

			print "Comparing: ",current.getData(), "Item", item
			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", count
				found = True
				break

			current = current.getNext()
			count  += 1

		if not found:
			print "Item: ", item, "Was Not Found On List"

		return found

	def traversal(self):
		current = self.front
		count    = 1

		print "Traversing List ..."	
		while current != None:

			print count, hex(id(current)),current.getData(), hex(id(current.getPrev())), hex(id(current.getNext()))
			#print count, hex(id(current)),current.getData(), current.getPrev(), current.getNext()
			current = current.getPrev()
			count += 1

	def rev_traversal(self):
		current = self.head
		count    = 1

		print "Traversing List in Reverse: Yahoo..."	
		while current != None:

			print count, hex(id(current)),current.getData(), hex(id(current.getPrev())), hex(id(current.getNext()))
			#print count, hex(id(current)),current.getData(), current.getPrev(), current.getNext()
			current = current.getNext()
			count += 1


