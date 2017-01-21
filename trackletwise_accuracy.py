f = open('classified_test_new.txt','rb')
lines = f.readlines()
f.close()

f = open('tracklet_wise_prediction_new.txt','wb')
previous_tracklet_id = ''
current_tracklet_list=[0 for i in range(7)]
for line in lines:
	current_tracklet = line.split(' ')[0].split('_')
	current_tracklet_id = current_tracklet[0]+'_'+current_tracklet[1]
	label = int(line.split(' ')[1].replace('\n',''))
	
	if previous_tracklet_id != current_tracklet_id and previous_tracklet_id!='':
		if previous_tracklet_id=='1_59':
			print current_tracklet_list,previous_tracklet_id,current_tracklet_list.index(max(current_tracklet_list))
		f.write(previous_tracklet_id+' '+str(current_tracklet_list.index(max(current_tracklet_list)))+'\n')
		#print previous_tracklet_id,' ', current_tracklet_list.index(max(current_tracklet_list)) 
		current_tracklet_list=[0 for i in range(7)]
		current_tracklet_list[label]+=1
	else:
		current_tracklet_list[label]+=1

	previous_tracklet_id = current_tracklet_id

f.write(previous_tracklet_id+' '+str(current_tracklet_list.index(max(current_tracklet_list)))+'\n')
	#print current_tracklet_id
f.close()
