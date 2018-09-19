# function to check if a list is an additive
def additive_sequence(lists):
	i=0
	result=None
	while (i<len(lists)):
		if i+1 < len(lists) and i+2<len(lists):
			first,second,total = lists[i],lists[i+1],lists[i+2]
			if first+second != total:
				result=False
				break
			else:
				result = True
		i += 1
	return result
print(additive_sequence([6, 6, 12, 18, 30,48 ]))