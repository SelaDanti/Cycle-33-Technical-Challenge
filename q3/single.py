# function to find the element that does not appear thrice
def single_element(lists):
	item = None
	for list in lists:
		if lists.count(list) != 3:
			item = list
	return item
