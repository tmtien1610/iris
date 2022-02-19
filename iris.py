import pandas as pd
from sklearn import tree
# Đọc tập tin json chứa tập dữ liệu iris
iris = pd.read_csv('iris.csv')
y = iris.variety
X = iris.drop(columns=['variety'])
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = tree.DecisionTreeClassifier(criterion="gini")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

def predict_iris(sl, sw, pl, pw):
    columns=["sepal.length", "sepal.width", "petal.length", "petal.width"]
    data = [[sl, sw, pl, pw]]
    df=pd.DataFrame(data,columns=columns)
    y_pred = model.predict(df)
    return y_pred
