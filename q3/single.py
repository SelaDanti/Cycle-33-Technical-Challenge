# function to find the element that does not appear thrice
def triple_check(lists):
	item = []
	list_set = set(lists)
	for lst in list_set:
		if lists.count(lst) != 3 and lists.count(lst) != 1:
			item = 'Invalid List'
			break
		if lists.count(lst) == 1:
			item.append(lst)
	if len(item) == 1:
		return item[0]
	else:
		return 'Invalid list'


