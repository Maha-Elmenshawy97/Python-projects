from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc


digits=datasets.load_digits()
features=digits.data
labels=digits.target

clf=SVC(gamma=0.001)
clf.fit(features,labels)  

#print(clf.predict([features[-2]]))


img=misc.imread("digit.jpg")
img=misc.imresize(img,(8,8))
img=img.astype(digits.images.dtype)
img=misc.bytescale(img,high=16,low=0)

 #print(features[-1]) 
#print(img)


x_test=[]

for eachrow in img:
    for eachpixel in eachrow:
        x_test.append(sum(eachpixel)/3.0)
        


print(clf.predict([x_test]))

