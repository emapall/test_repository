import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

labels = ['LAYING', 'SITTING', 'STANDING', 'WALKING', 'WALKUPS', 'WALKDWN']

fake_variable = ['WALKING']

frequency = 50.0
window_len = 1
window_pass = 0.5



frequency = 50.0
window_len = 1
window_pass = 0.5

for i in fake_variable:
	filename = "./data_sample/Subject_2_"+i+".txt"
	part_data=np.loadtxt(filename)
	begin = 0
	end = begin+ (window_pass*frequency)
	while(end < part_data.shape[0]):  #mean, std, max/min, medium, norm: FEATURE EXTRACTING
		_avg= part_data[begin:end, :].mean(axis=0)
		_std=np.std(part_data[begin:end, :],axis=0)
		_min=part_data[begin:end, :].min(axis=0)
		_max=np.max(part_data[begin:end, :],axis=0)
		_medium=np.median(part_data[begin:end, :], axis=0)
		_norm=np.linalg.norm(part_data[begin:end, :], axis=0)	

		if(begin==0):
			mean=_avg
			std=_std
			minimun=_min
			maximum=_max
			medium=_medium
			norm=_norm
		else:
			mean=np.vstack((mean,_avg))
			std=np.vstack((std,_std))	
			minimum=np.vstack((minimun,_min))
			maximum=np.vstack((maximum,_max))
			medium=np.vstack((medium,_medium))
			norm=np.vstack((norm,_norm))
		
		begin=end
		end=end = begin+ (window_pass*frequency)

	plt.figure()
	plt.plot(mean)
	plt.show()	
	
out_mean=[" "," "," "," "]

for i in range(mean.shape[0]):
	if (i==0):
		out_mean=[]
	
