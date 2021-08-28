from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
import pickle


# data=pd.read_csv('C:/Users/Jhanvee Khola/OneDrive/Desktop/Try IT Workshop/users/static/stroke.csv')
# lc=LabelEncoder()
# encod_gender=data['gender'].values
# encod_gender=lc.fit_transform(encod_gender)
# encod_marr=data['ever_married'].values
# encod_marr=lc.fit_transform(encod_marr)
# encod_work=data['work_type'].values
# encod_work=lc.fit_transform(encod_work)
# encod_resi=data['Residence_type'].values
# encod_resi=lc.fit_transform(encod_resi)
# encod_smok=data['smoking_status'].values
# encod_smok=lc.fit_transform(encod_smok)
# encod_bmi=data['bmi'].values
# encod_bmi=lc.fit_transform(encod_bmi)
# encod_age=data['age'].values
# encod_hyp=data['hypertension'].values
# encod_hear=data['heart_disease'].values
# encod_gluc=data['avg_glucose_level'].values
# y=data.iloc[:,11].values
# x=np.vstack((encod_gender,encod_age,encod_hyp,encod_hear,encod_marr,encod_work,encod_resi,encod_gluc,encod_bmi,encod_smok))
# x=x.transpose()
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# lr=LogisticRegression(solver='lbfgs',max_iter=10000)
# lrg=lr.fit(x_train,y_train)
# pickle.dump(lrg, open('data.pkl','wb'))

df = pd.read_excel('C:/Users/Jhanvee Khola/OneDrive/Desktop/Codes/IT Workshop/users/static/cancer.xlsx')
y=df.iloc[:,24].values
lb=LabelEncoder()
y=lb.fit_transform(y)
x=df.iloc[:,1:24].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lr=LogisticRegression(solver='lbfgs',max_iter=10000)
lrg=lr.fit(x_train,y_train)
pickle.dump(lrg, open('dataCan.pkl','wb'))