def fwrite(file, L):
	channel=open(file,'w')
	for i in L:
		channel.write(i +'\n')
	channel.close()

fwrite('filante',['hi','my name is mario','and i am a','farmer'])

