import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

labels = ['LAYING', 'SITTING', 'STANDING', 'WALKING', 'WALKUPS', 'WALKDWN']

frequency = 50.0
window_len = 1
window_pass = 0.5

data_labels=["adjsdj"]


def andrewtegify(whatever, start, end):
    duration = start - end
    max = np.amax(whatever) * duration
    min = np.amin(whatever) * duration
    steps = abs(duration / len(whatever))
    axis = np.arange(start, end, steps)
    while len(whatever) != len(axis):
        if len(whatever) > len(axis): 
            #print 'add'
            axis = np.append(axis, (axis[len(axis)-1]+steps))
        elif len(whatever) < len(axis): 
            #print 'remove'
            axis = np.delete(axis, (len(axis) - 1))
        #print str(len(whatever)) + ' ' +  str(len(axis))
        
    totar = 0
    if max < 0 and min < 0:
        va = min - max
        tarea = scipy.integrate.simps(whatever, axis)
        totar = va / tarea
    elif max > 0 and min < 0:
        va = max - min
        tarea = scipy.integrate.simps(whatever, axis)
        totar = va / tarea
        
    elif max > 0 and min > 0:
        va = max - min
        tarea = scipy.integrate.simps(whatever, axis)
        totar = va / tarea
    return totar
    



for i in labels:
	filename = "./data_sample/Subject_2_"+i+".txt"
	part_data=np.loadtxt(filename)
	begin = 0
	end = begin+ (window_pass*frequency)
	while(end < part_data.shape[0]):  #mean, std, max/min, medium, norm: FEATURE EXTRACTING
		_avg= part_data[begin:end, :].mean(axis=0)
		_std=np.std(part_data[begin:end, :],axis=0)
 		_integ = andrewtegify(part_data[begin:end], begin, end)
		_min=part_data[begin:end, :].min(axis=0)
		_max=np.max(part_data[begin:end, :],axis=0)
		_medium=np.median(part_data[begin:end, :], axis=0)
		_norm=np.linalg.norm(part_data[begin:end, :], axis=0)	
		
		if(begin==0 and i=="LAYING"):
			mean=_avg
			std=_integ
			minimun=_min
			maximum=_max
			medium=_medium
			norm=_norm
			data_labels[0]=i
			
		else:
			mean=np.vstack((mean,_avg))
			std=np.vstack((std,_integ))	
			minimum=np.vstack((minimun,_min))
			maximum=np.vstack((maximum,_max))
			medium=np.vstack((medium,_medium))
			norm=np.vstack((norm,_norm))
			data_labels.append(i)
		
		begin=end
		end=end = begin+ (window_pass*frequency)
	
	plt.plot(mean)
	plt.title(i)
	plt.show()


	
#MEAN OUTPUT
out_mean=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_mean=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_mean=np.vstack((out_mean,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("mean",out_mean)

#STD OUTPUT

out_std=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_std=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_std=np.vstack((out_std,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("std",out_std)

#MAX OUTPUT

out_max=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_max=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_max=np.vstack((out_max,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("max",out_max)
	

#MINIMUM OUTPUT
out_min=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_min=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_min=np.vstack((out_min,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("min",out_min)	

#MEDIUM OUTPUT


out_medium=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_medium=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_medium=np.vstack((out_medium,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("mean",out_medium)


#NORM OUTPUT

out_norm=np.array(["","","",""])	

for i in range(mean.shape[0]):
	if (i==0):
		out_norm=np.array([ data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ])
	else:
		out_norm=np.vstack((out_norm,[  data_labels[i], str(mean[i,0]),str(mean[i,1]),str(mean[i,2]) ]))

np.save("norm",out_norm)

	
#do the output:whether to output labels on x asis of the plot, or to output just a table like 
# LABELS (eg: stand, run, walk), avg:xyz, maximun: xyx, minimum: xyz, norm: xyz, std:xyz.....
#SO THAT YOU CAN PUT THEM EASYLY INTO A DATAFRAME, LISTS OR WAHTHEVER!	


