import caffe
import numpy as np



net = caffe.Classifier('/mnt/data/network_deploy.prototxt', '/mnt/data/_iter_6000.caffemodel',mean=np.load('/mnt/data/out.npy').mean(1).mean(1),channel_swap=(2,1,0),raw_scale=255,image_dims=(227, 227))

f = open('/mnt/data/test-data-new.txt','rb')
lines = f.readlines()
f.close()

f = open('classified_test.txt','wb')

i=0
for line in lines:
  imagename = line.split(' ')[0]
  input_image = caffe.io.load_image('/mnt/data/test/'+imagename)
  prediction = net.predict([input_image])
  label = prediction[0].argmax()
  i+=1
  f.write(imagename+' '+str(label)+'\n')
  if i%100==0:
    print i
    print imagename,label

f.close()
