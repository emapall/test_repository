import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import matplotlib as pls
from sklearn.datasets import load_iris
clear
iris=load_iris()
type(iris)
iris
iris.target
iris.data.shape()
iris.data.shape
iris.target.shape
x=iris.data[:,:2]
x
x_train=x[:90]
x_train.shape()
x_train.shape
x
x_train
x_train=x[:90,:]
x_train-shape
x_train.shape
y=iris.target
y_train=y[:90]
y_train
iris.target.shape
from sklear import cross_validation
from sklearn import cross_validation
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
x_train
y_train
#at this point, we have split the dataset of the iris with sthe split function, and (an a return) we have (put) some array which are actually the test: x_trai, x_test, ecc. essentialy, the funcion is just like a ""random sort""

from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier() #parentesi!!
clf
clf_fitted=clf.fit(x_train,y_train) 
#CLF FITTED IS ACTUALLY A DECISION TREE (OBJ?ALG?CLASS? WHO CARES) who has been set (=fitted) which is, the parameters have been set. now we may test it !
clf_fitted
type(clf_fitted)
clf_fitted.score(x_test, y_test)
from sklearn import svm
clf=svm.linearSVC(C=1)
clf=svm.LinearSVC(C=1)
clf_fitted=clf.fit(x_train,y_train)
clf_fitted.score(x_test, y_test)
cross_validation.cross_val_score(clf,x,y,cv=5)
scores=cross_validation.cross_val_score(clf,x,y,cv=5)
scores
scores=cross_validation.cross_val_score(clf,x,y,cv=100)
scores
scores=cross_validation.cross_val_score(clf,x,y,cv=10)
scores
print "accuracy: %0.2f (+/- %0.2f) " % (scores.mean(), scores.std()*2))
print "accuracy: %0.2f (+/- %0.2f) " % (scores.mean(), scores.std()*2)
clf=svm.LinearSVC(C=10)
scores=cross_validation.cross_val_score(clf,x,y,cv=10)
print "accuracy: %0.2f (+/- %0.2f) " % (scores.mean(), scores.std()*2)
clist=[10**2 for i in range (-5,5)
]
clist
clist=[10**i for i in range (-5,5)
]
clist
for c in clist:
    clf=svm.LinearSVC(C=c)
    scores=cross_validation.cross_val_score(clf,x,y,cv=5)
    print "accuracy: %0.2f (+/- %0.2f) " % (scores.mean(), scores.std()*2)
%history -f ~/Work/python_m_learing.py
%history -f "~/Work/python_m_learing.py"
%history -f "~/Work/"python_m_learing.py
%history -f "~/Work/"python_m_learing.py
%history -f python_m_learing.py
