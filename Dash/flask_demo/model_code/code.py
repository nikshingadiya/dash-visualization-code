import datacleaner as dc
import numpy
import  scipy.stats as st
import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, StratifiedKFold
import  pickle
# data import
fd_dlvry = pd.read_csv('Dataset_Banglore_food_delivery/onlinedeliverydata.csv')
fd_ori = fd_dlvry.copy()

fd_dlvry.drop(['Pin code', 'longitude', 'latitude', 'Reviews'], axis=1, inplace=True)

fd_dlvry['Output'] = fd_dlvry['Output'].replace({'Yes': 1, 'No': 0})

# import  datacleaner as dc # pip install datacleaner
dc.autoclean(fd_dlvry).head()
# feature Selection

l1 = []
for i in fd_ori.columns:
    if i not in ['latitude', 'longitude', 'Pin code', 'Output', 'Reviews']:
        '''we are not using lat and long because in EDA all location diffrent (reference dtale lib)'''
        df = pd.crosstab(fd_ori['Output'], fd_ori[i])
        stat, p, dof, expected = st.chi2_contingency(df, correction=True)

        deno = sum(df.sum())
        x = numpy.sqrt(stat / deno)
        if (x > 0.40):  # thresold
            l1.append((i, x))

#  feature seperate

basic_f0 = []
for i in l1:
    basic_f0.append(i[0])
X = fd_dlvry[basic_f0]
y = fd_dlvry.iloc[:, -1]
X_ori=X.copy()
y_ori=y.copy()

# make class  balance
nm = RandomOverSampler()
X, y =nm.fit_resample(X,y)


# train_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Build model
clf = RandomForestClassifier(max_depth=3, min_samples_split=4)
clf.fit(X_train, y_train)
print("Score: ", clf.score(X_test, y_test))

# predict
y_pred = clf.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print()
print("Classification Report:\n", classification_report(y_test, y_pred))

# Cross Validation
lst_accu_stratified = []
x = 0

skf = StratifiedKFold(n_splits=12, shuffle=True, random_state=1)
for train_index, test_index in skf.split(X_ori, y_ori):
    x_train_fold, x_test_fold = X.loc[train_index, :], X.loc[test_index, :]
    y_train_fold, y_test_fold = y[train_index], y[test_index]
    clf.fit(x_train_fold, y_train_fold)
    lst_accu_stratified.append(clf.score(x_test_fold, y_test_fold))

print('List of possible accuracy:', lst_accu_stratified)
print('\nMaximum Accuracy That can be obtained from this model is:',
      max(lst_accu_stratified) * 100, '%')
print('\nMinimum Accuracy:',
      min(lst_accu_stratified) * 100, '%')
print('\nAverage Accuracy That can be obtained from this model is::', np.mean(lst_accu_stratified))
print('\n Median Accuracy That can be obtained from this model is::', np.median(lst_accu_stratified))
print('\nStandard Deviation is:', np.std(lst_accu_stratified))


# Build Running
pickle.dump(clf, open('model.pkl','wb'))

# Cross Check
model = pickle.load(open('model.pkl','rb'))

print(model.predict(np.array([20,2,3,1,3,2,1,1,2,3]).reshape(1,-1)))
