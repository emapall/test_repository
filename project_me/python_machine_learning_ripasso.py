run project.py
meanb
mean
import pandas as pd
ll
out_mean
label=np.array(out_mean[:,0])
label
mean = np.array(out_mean[:,1:].astype(float))
mean
out_std
std
std=np.array(out_std[:,1:].astype(float))
std
data=np.hstack((mean,std))
data
data.shape
%paste
x_train, x_test, l_train, l_test = cross_validation.train_test_split(data, labels, test_size=0.2)
labels.shape
labels
label
x_train, x_test, l_train, l_test = cross_validation.train_test_split(data, label, test_size=0.2)
x_test
from sklearn.tree import DecisionTreeClassifier

#from here now, we will build the model for selection

clf = DecisionTreeClassifier() #!!!!!!!()!!!!!

clf_fitted= clf.fit(x_train, l_train) #"FIT" THE  stuff	
help (pd.DecisionTreeClassifier)     #try to undrestand something out of that
help (DecisionTreeClassifier)  #try again
help (DecisionTreeClassifier.fit)  #ok i'm stupid
i don't even know what i'm asking!!!!!
dispicable m....ph no wait, it was
clf_fitted= clf.fit(x_train, l_train)
clf = DecisionTreeClassifier  #yeah, why don't we do again the same mistake a lot of time?
clf_fitted= clf.fit(x_train, l_train)
clf_fitted= clf.fit(x_train, l_train)
help(clf.fit)
clf_fitted= clf.fit(self,x_train, l_train)
help(clf.fit)
clf_fitted= clf.fit(clf,x_train, l_train)
help(clf.fit)
clf_fitted= clf.fit(x_train, l_train)
clf_fitted= clf.fit(clf,x_train, l_train)
clf
type(clf)
clf=DecisionTreeClassifier()
clf
clf_fitted= clf.fit(clf,x_train, l_train)
clf_fitted= clf.fit(x_train, l_train)
clf_fitted
cross_validation.cross_val_score(clf_fitted,x,y,cv=5)
data
label
cross_validation.cross_val_score(clf_fitted,data,lablel,cv=5)
cross_validation.cross_val_score(clf_fitted,data,label,cv=5)
%history
%history --help
pwd
%history-f python_machine_learning_ripasso.py
