# train_models.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv('heart_disease_data.csv')  # Ensure you have this dataset

# Define features and target
X = data.drop('target', axis=1)  # 'target' is the label
y = data['target']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
knn = KNeighborsClassifier(n_neighbors=8)
svc = SVC(kernel='rbf')
sgd = SGDClassifier(loss='hinge')
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)

# Train models
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
sgd.fit(X_train, y_train)
mlp.fit(X_train, y_train)

# Evaluate and save models
models = {'KNN': knn, 'SVC': svc, 'SGD': sgd, 'MLP': mlp}
for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f'{name} Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')
    joblib.dump(model, f'{name}_model.pkl')
