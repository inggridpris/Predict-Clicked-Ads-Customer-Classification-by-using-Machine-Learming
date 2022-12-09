# -*- coding: utf-8 -*-
"""Predict Clicked Ads Customer Classification by Using Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GD859o5u4Sfq62qcQLG9PkcGw84FyiQ6
"""

from google.colab import drive
drive.mount('/content/drive')

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print('Numpy Version:', np.__version__)
print('Pandas Version:', pd.__version__)
print('Seaborn Version:', sns.__version__)

from matplotlib import rcParams
rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

df= pd.read_csv('/content/drive/My Drive/Predict Clicked Ads Customer by Using Machine Learning/Clicked Ads Dataset.csv')

df = pd.read_csv('Clicked Ads Dataset.csv')

df

df.info()

df.sample(5)

nums=['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage']
cats=['Male','Clicked on Ad','city','province','category']

df[nums].describe()

df[cats].describe()

for col in cats :
    print(f'''Value count kolom{col}:''')
    print(df[col].value_counts())
    print()

features=nums
plt.figure(figsize=(8,10))
for i in range (0, len(features)):
    plt.subplot(3,5,i+1)
    sns.boxplot(y=df[features[i]], color='blue', orient='v')
    plt.tight_layout()

features = nums
plt.figure(figsize=(12, 10))
for i in range(0, len(nums)):
    plt.subplot(4, 4, i+1)
    sns.kdeplot(x=df[features[i]], color='green')
    plt.xlabel(features[i])
    plt.tight_layout()

plt.figure(figsize=(12, 10))
for i in range(0, len(cats)):
    plt.subplot(3, 3, i+1)
    sns.countplot(x = df[cats[i]], color='green', orient='v')
    plt.tight_layout()

df.corr()

plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), cmap='Blues', annot=True, fmt='.2f')
plt.savefig('correlation.jpeg', dpi=100)

plt.figure(figsize=(20, 20))
sns.pairplot(df[nums], diag_kind='kde')

sns.scatterplot(x='Daily Time Spent on Site', y='Daily Internet Usage', hue='Clicked on Ad', data=df)
plt.savefig('daily time dengan daily internet.jpg', dpi=100)

sns.scatterplot(x='Age', y='Daily Internet Usage', hue='Clicked on Ad', data=df)
plt.savefig('age dengan daily internet.jpg', dpi=100)

sns.scatterplot(x='Daily Time Spent on Site', y='Age', hue='Clicked on Ad', data=df)
plt.savefig('daily internet dengan age.jpg', dpi=100)

features = cats
plt.figure(figsize=(10, 25))
for i in range(0, len(features)):
    plt.subplot(8, 1, i+1) 
    sns.countplot(x=features[i], data=df,  palette="seismic", hue="Clicked on Ad")
    #plt.xlabel(features[i])
    plt.tight_layout()

features = nums
plt.figure(figsize=(10, 25))
for i in range(0, len(features)):
    plt.subplot(10, 1, i+1) 
    sns.countplot(x=features[i], data=df,  palette="seismic", hue="Clicked on Ad")
    #plt.xlabel(features[i])
    plt.tight_layout()

df.info()

pip install dython

from dython.nominal import associations, identify_nominal_columns
associations(df[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male','Clicked on Ad','city','province','category']], figsize=(10,10), nan_strategy='drop_samples')
plt.savefig('correlation.jpeg')

df1=df.copy()

df1.info()

df1.isna().sum()

df1['Daily Time Spent on Site']=df1['Daily Time Spent on Site'].fillna(df1['Daily Time Spent on Site'].mean())
df1['Area Income']=df1['Area Income'].fillna(df1['Area Income'].mean())
df1['Daily Internet Usage']=df1['Daily Internet Usage'].fillna(df1['Daily Internet Usage'].mean())
df1['Male']=df1['Male'].fillna('Perempuan')

df1.isna().sum()

df1.duplicated().sum()

df1['date']=pd.to_datetime(df1['Timestamp'])

df1['date']

df1['year']=df1['date'].dt.year
df1['month']=df1['date'].dt.month
df1['day']=df1['date'].dt.day

df1['weekday']=df1['date'].dt.weekday

df1['weekend']=df1['weekday']>=5

df1['week_number']=df1['date'].dt.week

df1.info()

df1.sample(5)

mapping_male={'Perempuan':0, 'Laki-Laki':1}
df1['Male']=df1['Male'].map(mapping_male)

df1.info()

mapping_click={'No':0, 'Yes':1}
df1['Clicked on Ad']=df1['Clicked on Ad'].map(mapping_click)

df1.info()

cats_one=['city','province','category']
for cats_one in ['city','province','category']:
    onehots = pd.get_dummies(df1[cats_one],prefix=cats_one)
    df1=df1.join(onehots)

df1.info()

df2 = df1.drop(columns=['Unnamed: 0','city','weekend','province','category','date','Timestamp'])

df2.info()

df2['Daily Time Spent on Site']= df2['Daily Time Spent on Site'].astype('int')
df2['Area Income']= df2['Area Income'].astype('int')
df2['Daily Internet Usage']= df2['Daily Internet Usage'].astype('int')

df2.info()

corrmat = df2.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(25,25))
g=sns.heatmap(df2[top_corr_features].corr(),annot=True,cmap="RdYlGn")

a = corrmat['Clicked on Ad']
hasil = a[(a>0.05)|(a<-0.05)]
hasil

df3_selection=df2[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur','Clicked on Ad']]

"""### Before Normalisasi"""

X = df3_selection[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur']]
y = df3_selection['Clicked on Ad'] # target / label

#Splitting the data into Train and Test
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42, shuffle=False)

x_data= df3_selection[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur']]
y_data = df3_selection['Clicked on Ad']

x_data

y_data

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def eval_classification(model):
    y_pred = model.predict(X_test)
    print("Accuracy (Test Set): %.2f" % accuracy_score(y_test, y_pred))
    print("Precision (Test Set): %.2f" % precision_score(y_test, y_pred))
    print("Recall (Test Set): %.2f" % recall_score(y_test, y_pred))
    print("F1-Score (Test Set): %.2f" % f1_score(y_test, y_pred))
    print('AUC:'+ str(roc_auc_score(y_test, y_pred)))

def show_feature_importance(model):
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
    ax.invert_yaxis()

    plt.xlabel('score')
    plt.ylabel('feature')
    plt.title('feature importance score')

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)

eval_classification(lr)

print('Train score: ' + str(lr.score(X_train, y_train))) #accuracy
print('Test score: ' + str(lr.score(X_test, y_test))) #accuracy

logres = LogisticRegression(penalty='l2', C=0.0001, solver='lbfgs', random_state=42)
logres.fit(X_train, y_train)
y_pred = logres.predict(X_test)
print (y_pred)

import math

feature_names = X_train.columns.to_list()

#Get the scores
score = logres.score(X_train.values, y_train)
print(score)
w0 = logres.intercept_[0]
w = logres.coef_[0]

feature_importance = pd.DataFrame(feature_names, columns = ['feature'])
feature_importance['importance'] = pow(math.e, w)
feature_importance = feature_importance.sort_values(by=['importance'],ascending=False)
feature_importance = feature_importance[:8].sort_values(by=['importance'], ascending=False)

#Visualization
ax = feature_importance.sort_values(by=['importance'], ascending=True).plot.barh(x='feature', y='importance')

plt.title('Important Feature')
plt.show()

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

eval_classification(dt)

print('Train score: ' + str(dt.score(X_train, y_train))) #accuracy
print('Test score:' + str(dt.score(X_test, y_test))) #accuracy

feat_importances = pd.Series(dt.feature_importances_, index=X_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from sklearn.ensemble import AdaBoostClassifier
ab = AdaBoostClassifier(random_state=42)
ab.fit(X_train, y_train)

eval_classification(ab)

print('Train score: ' + str(ab.score(X_train, y_train))) #accuracy
print('Test score:' + str(ab.score(X_test, y_test)))

feat_importances = pd.Series(ab.feature_importances_, index=X_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

plt.savefig('futureimportanceab.jpeg', dpi=200)

from xgboost import XGBClassifier
xg = XGBClassifier(random_state=42)
xg.fit(X_train, y_train)

eval_classification(xg)

print('Train score: ' + str(xg.score(X_train, y_train))) #accuracy
print('Test score:' + str(xg.score(X_test, y_test))) #accuracy

feat_importances = pd.Series(xg.feature_importances_, index=X_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

eval_classification(rf)

print('Train score: ' + str(rf.score(X_train, y_train))) #accuracy
print('Test score:' + str(rf.score(X_test, y_test)))

feat_importances = pd.Series(rf.feature_importances_, index=X_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')



"""### After Normalisasi"""

df3=df2[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur']]

# copy the data
df_z_scaled = df3.copy()
  
# apply normalization techniques
for column in df_z_scaled.columns:
    df_z_scaled[column] = (df_z_scaled[column] -
                           df_z_scaled[column].mean()) / df_z_scaled[column].std()    
  
# view normalized data   
display(df_z_scaled)

import matplotlib.pyplot as plt
df_z_scaled.plot(kind='bar')

df_z_scaled.info()

x1= df_z_scaled[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur']]
y1 = df3_selection['Clicked on Ad']
#Splitting the data into Train and Test
from sklearn.model_selection import train_test_split 
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size = 0.3, random_state = 42)

x_data1= df_z_scaled[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','city_Balikpapan','city_Cimahi','city_Jakarta Pusat','city_Malang','city_Serang','city_Tangerang Selatan','province_Banten','province_Jawa Barat','province_Kalimantan Timur']]
y_data1 = df3_selection['Clicked on Ad']

x_data1

y_data1

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def eval_classification(model):
    y1_pred = model.predict(x1_test)
    print("Accuracy (Test Set): %.2f" % accuracy_score(y1_test, y1_pred))
    print("Precision (Test Set): %.2f" % precision_score(y1_test, y1_pred))
    print("Recall (Test Set): %.2f" % recall_score(y1_test, y1_pred))
    print("F1-Score (Test Set): %.2f" % f1_score(y1_test, y1_pred))
    print('AUC:'+ str(roc_auc_score(y1_test, y1_pred)))

def show_feature_importance(model):
    feat_importances = pd.Series(model.feature_importances_, index=x1.columns)
    ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
    ax.invert_yaxis()

    plt.xlabel('score')
    plt.ylabel('feature')
    plt.title('feature importance score')

y1_train

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=42)
lr.fit(x1_train, y1_train)

eval_classification(lr)

print('Train score: ' + str(lr.score(x1_train, y1_train))) #accuracy
print('Test score: ' + str(lr.score(x1_test, y1_test))) #accuracy

logres = LogisticRegression(penalty='l2', C=0.0001, solver='lbfgs', random_state=42)
logres.fit(X_train, y_train)
y_pred = logres.predict(X_test)
print (y_pred)

import math

feature_names = x1_train.columns.to_list()

#Get the scores
score = logres.score(x1_train.values, y_train)
print(score)
w0 = logres.intercept_[0]
w = logres.coef_[0]

feature_importance = pd.DataFrame(feature_names, columns = ['feature'])
feature_importance['importance'] = pow(math.e, w)
feature_importance = feature_importance.sort_values(by=['importance'],ascending=False)
feature_importance = feature_importance[:8].sort_values(by=['importance'], ascending=False)

#Visualization
ax = feature_importance.sort_values(by=['importance'], ascending=True).plot.barh(x='feature', y='importance')

plt.title('Important Feature')
plt.show()

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x1_train, y1_train)

eval_classification(dt)

print('Train score: ' + str(dt.score(x1_train, y1_train))) #accuracy
print('Test score:' + str(dt.score(x1_test, y1_test))) #accuracy

feat_importances = pd.Series(dt.feature_importances_, index=x1_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from sklearn.ensemble import AdaBoostClassifier
ab = AdaBoostClassifier(random_state=42)
ab.fit(x1_train, y1_train)

eval_classification(ab)

print('Train score: ' + str(ab.score(x1_train, y1_train))) #accuracy
print('Test score:' + str(ab.score(x1_test, y1_test)))

feat_importances = pd.Series(ab.feature_importances_, index=x1_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from xgboost import XGBClassifier
xg = XGBClassifier(random_state=42)
xg.fit(x1_train, y1_train)

eval_classification(xg)

print('Train score: ' + str(xg.score(x1_train, y1_train))) #accuracy
print('Test score:' + str(xg.score(x1_test, y1_test))) #accuracy

feat_importances = pd.Series(xg.feature_importances_, index=x1_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=42)
rf.fit(x1_train, y1_train)

eval_classification(rf)

print('Train score: ' + str(rf.score(x1_train, y1_train))) #accuracy
print('Test score:' + str(rf.score(x1_test, y1_test)))

feat_importances = pd.Series(rf.feature_importances_, index=x1_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')



# Split Feature and Label
X_imp = X_train[['Area Income','Daily Time Spent on Site','Daily Internet Usage','Age','city_Tangerang Selatan']]
y_imp = y_train # target / label

#Splitting the data into Train and Test
from sklearn.model_selection import train_test_split 
X_train_imp, X_test_imp, y_train_imp, y_test_imp = train_test_split(X_imp, y_imp, test_size = 0.3, random_state = 42)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def eval_class(model):
    y_pred_imp = model.predict(X_test_imp)
    print("Accuracy (Test Set): %.2f" % accuracy_score(y_test_imp, y_pred_imp))
    print("Precision (Test Set): %.2f" % precision_score(y_test_imp, y_pred_imp))
    print("Recall (Test Set): %.2f" % recall_score(y_test_imp, y_pred_imp))
    print("F1-Score (Test Set): %.2f" % f1_score(y_test_imp, y_pred_imp))
    print('AUC:'+ str(roc_auc_score(y_test_imp, y_pred_imp)))

def show_feature_importance(model):
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
    ax.invert_yaxis()

    plt.xlabel('score')
    plt.ylabel('feature')
    plt.title('feature importance score')

def show_best_hyperparameter(model, hyperparameters):
    for key, value in hyperparameters.items() :
        print('Best '+key+':', model.get_params()[key])

from sklearn.ensemble import AdaBoostClassifier
ab_imp = AdaBoostClassifier(random_state=42)
ab_imp.fit(X_train_imp,y_train_imp)

eval_class(ab_imp)

from sklearn.metrics import confusion_matrix

#Generate the confusion matrix
y_pred_c = ab_imp.predict(X_test_imp)
cf_matrix = confusion_matrix(y_test_imp, y_pred_c)

print(cf_matrix)

group_names = ['True Negative','False Positive','False Negative','True Positive']
group_counts = ["{0:0.0f}".format(value) for value in
cf_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')
ax.set_title('Confusion Matrix\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])
## Display the visualization of the Confusion Matrix.
plt.show()

df4=df3_selection[['Area Income','Daily Time Spent on Site','Daily Internet Usage','Age','city_Tangerang Selatan','Clicked on Ad']]

df4.info()

df4.describe()

from dython.nominal import associations, identify_nominal_columns
associations(df4[['Area Income','Daily Time Spent on Site','Daily Internet Usage','Age','city_Tangerang Selatan','Clicked on Ad']], figsize=(10,10), nan_strategy='drop_samples')
plt.savefig('correlation.jpeg')

df4.corr()

sns.scatterplot(x='Daily Time Spent on Site', y='Daily Internet Usage', hue='Clicked on Ad', data=df4)

sns.scatterplot(x='Area Income', y='Daily Internet Usage', hue='Clicked on Ad', data=df4)

sns.scatterplot(x='Age', y='Daily Internet Usage', hue='Clicked on Ad', data=df4)

sns.scatterplot(x='city_Tangerang Selatan', y='Daily Internet Usage', hue='Clicked on Ad', data=df4)

