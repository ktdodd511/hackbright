shopping_list = []

def add():
	while(True):
		print "Type exit to stop adding items."
		items = raw_input("Enter an item: ")

		if items == "exit":
			break

		if items in shopping_list:
			print("You already added this!")
		else:
			shopping_list.append(items)

	abc_order()	
	
	print "Your items are:", shopping_list


def abc_order():
	shopping_list.sort()


if __name__== '__main__':
	add()