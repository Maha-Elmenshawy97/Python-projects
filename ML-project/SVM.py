import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy

col = ['zip_code', 'title', 'status', 'ratio', 'unique']
data=pd.read_csv('steam.csv',sep=',',header=None,names=col)

#non_unique=data.loc[data.duplicated()]

le=LabelEncoder()
data['status'] = le.fit_transform(data.status)
data['title'] = le.fit_transform(data.title)

##separate array into input and output components
array = data.values
X = array[:,:-1]
Y = array[:,-1]

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
numpy.set_printoptions(precision=3)
#print(rescaledX[0:5,:])

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.5, random_state=0)

from sklearn import svm
clf = svm.SVC(kernel='linear',C=1, gamma=1) # Linear Kernel
#Train the model using the training sets
clf.fit(X_train, y_train)
#predicting the results on the training & tasting set
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

from sklearn import metrics
# Model Accuracy: how often is the classifier correct?
print("========================================")
print("test_Accuracy:",metrics.accuracy_score(y_test, y_test_pred))
print("train_Accuracy:",metrics.accuracy_score(y_train, y_train_pred))


'''
def success_ratio(cm):
    total = cm[0][0] + cm[1][0] + cm[0][1] + cm[1][1]
    return 100*(cm[0][0] + cm[1][1]) / total


from sklearn.metrics import confusion_matrix
cm_train = confusion_matrix(y_train, y_train_pred)
cm_test = confusion_matrix(y_test, y_test_pred)

print("Training set confusion matrix : \n"+str(cm_train))
print("Success ratio on training set : "+str(success_ratio(cm=cm_train))+"%")
print("Test set confusion matrix : \n"+str(cm_test))
print("Success ratio on test set : "+str(success_ratio(cm=cm_test))+"%")
'''