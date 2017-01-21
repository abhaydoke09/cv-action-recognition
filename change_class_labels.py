f = open('labels.txt','rb')
lines = f.readlines()
f.close()

f = open('labels-new.txt','wb')
for line in lines:
	line = line.replace('\n','')
	filename,label = line.split(' ')
	f.write(filename+' '+str(int(label)-1)+'\n')

f.close()