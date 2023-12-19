from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset (you can replace this with your own dataset)
digits = load_digits()
X, y = digits.data, digits.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Individual Decision Tree (Weak Classifier)
tree_classifier = DecisionTreeClassifier(max_depth=3)
tree_classifier.fit(X_train, y_train)

# Predictions using the individual Decision Tree
y_tree_pred = tree_classifier.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_tree_pred)
print(f'Accuracy of Individual Decision Tree: {accuracy_tree:.2%}')

# Adaboost Ensemble of Decision Trees
adaboost_classifier = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, random_state=42)
adaboost_classifier.fit(X_train, y_train)

# Predictions using the Adaboost Ensemble
y_adaboost_pred = adaboost_classifier.predict(X_test)
accuracy_adaboost = accuracy_score(y_test, y_adaboost_pred)
print(f'Accuracy of Adaboost Ensemble: {accuracy_adaboost:.2%}')

