from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


data = pd.DataFrame({"city":["Bangalore","chennai","chennai","chennai","Bangalore","Bangalore","chennai"],
                     "job":["employed","student","employed","unemployed","employed","student","employed"],
                     "credit_limit":["1-2 lakhs","1 lakhs","2-3 lakhs","1 lakhs","1 lakhs","1 lakhs","2-3 lakhs"],
                     "age":["20","15","55","33","27","18","28"],
                     "y":["yes","yes","no","no","yes","no","yes"]}, 
                    columns=["city","job","credit_limit","age","y"])
                    
#features = data[["city","job","credit_limit","age","y"]]
#target = data["y"]                    
print(data)

#-----Prediction Accuracy------ 

label=LabelEncoder()
data["city"]=label.fit_transform(data["city"])
data["job"]=label.fit_transform(data["job"])
data["credit_limit"]=label.fit_transform(data["credit_limit"])
data["age"]=label.fit_transform(data["age"])
data["y"]=label.fit_transform(data["y"])

X= data.iloc[:,0:9]
Y= data.iloc[:,4]

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.3,random_state=100)
clf=DecisionTreeClassifier(criterion ='entropy').fit(x_train.astype(int),y_train.astype(int))
prediction=clf.predict(x_test)

print("--------------Prediction Accuracy-----------------")
print("The prediction accuracy is: {0} ".format(accuracy_score(y_test.astype(int),prediction)*100))


#------Tree----- 

def entropy(target_col): 
    elements,counts = np.unique(target_col,return_counts = True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

def InfoGain(data,split_attribute_name,target_name="y"): 
    total_entropy = entropy(data[target_name]) 
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)   
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))]) 
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def ID3(data,originaldata,features,target_attribute_name="y",parent_node_class = None):
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data)==0:
        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name],return_counts=True)[1])]
    elif len(features) ==0:
        return parent_node_class
    else:    
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])]
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features] 
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature:{}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data,data,features,target_attribute_name,parent_node_class)
            tree[best_feature][value] = subtree
        return(tree) 
         
                
T = ID3(data,data,data.columns[:-1])
print("-----------------Tree------------------")
print(T)
