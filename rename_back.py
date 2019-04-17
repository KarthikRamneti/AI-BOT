import numpy as np
import os
path = "/home/sai/Desktop/Project/new_back"
print path
filenames = os.listdir(path)
i=1
k1 = "rename_back.py"
k2 = "rename_back.pyc"
for f in filenames:
	if f!=k1 and f!=k2:
		a = "back"+str(i)+".wav"
		os.rename(f,a)
		i = i+1
		print a
	#a = "back"+str(i)+".wav"
	#os.rename(f,a)
	#i = i+1
	#print a
			

