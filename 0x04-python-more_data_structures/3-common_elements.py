#!/usr/bin/python3
def common_elements(set_1, set_2):
	commons = []
	for i in set_1:
		for k in set_2:
			if i == k and i not in commons:
				commons.append(i)
	return commons
