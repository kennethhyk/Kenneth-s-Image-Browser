L=['.DS_Store','imageBrowser1.py', 'imageBrowser2.py', 'One.gif', 'imageBrowser3.py','Seven.gif', 'Six.gif', 'Three.gif', 'Two.gif', 'Zero.gif']
x=len(L)-1
for i in reversed(L):
	print(x)
	print(L[x])
	if i.find('.gif') == -1:
		print('poped',L.pop(x))
	x=x-1

print(L)