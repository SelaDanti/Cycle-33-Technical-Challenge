def additive_sequence(lists):
	i=0
	result=None
	while (i<len(lists)):
		if i+1 < len(lists) and i+2<len(lists):
			first,second,other = lists[i],lists[i+1],lists[i+2]
			if first+second != other:
				result=False
				break
			else:
				result = True
		i += 1
	return result
