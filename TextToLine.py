from songline import Sendline
token = 'RnraCw5OSzn492JJ2OSL39p4oIkVvrBAtGCk4IkbQRE'
messenger = Sendline(token)

#messenger.sendtext()

#Pull data
checktwitter = ['elonmask','BillGates','cnnbrk','SpaceX']

for ct in checktwitter:
	TextToLine = ''
	post = TwitterPost(ct)
	print('--------------- {} -------------'.format(ct))
	TextToLine += '--------------- {} -------------\n'.format(ct)

	for p in post:
		print(p)
		TextToLine += p + '\n\n' #TextToLine = TextToLine + p
		print('=========')

	messenger.sendtext(TextToLine)


driver.close()
