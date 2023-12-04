import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

column_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv('./data/car_evaluation_dataset.csv',header=None,names=column_names)

# Summary statistics
summary_stats = df.describe()

# Save summary statistics to a file
summary_stats.to_csv('./results/summary_statistics.csv')

# Simple visualization (bar chart for 'class')
class_counts = df['class'].value_counts()
class_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribution of Car Evaluation Classes')
plt.xlabel('Evaluation Level')
plt.ylabel('Count')
plt.savefig('./results/class_distribution.png')
#plt.show()

# Split the data into features (X) and target variable (y)
X = df.drop('class', axis=1)
y = df['class']

# Convert categorical features to numerical using one-hot encoding
X_encoded = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train a Decision Tree classifier
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
conf_matrix_df = pd.DataFrame(conf_matrix, index=classifier.classes_, columns=classifier.classes_)
results_file_path = './results/classification_results.txt'
with open(results_file_path, 'w') as results_file:
    results_file.write(f"Accuracy: {accuracy:.2f}\n\n")
    results_file.write("Confusion Matrix:\n")
    results_file.write(conf_matrix_df.to_string())

# Save the confusion matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=classifier.classes_, yticklabels=classifier.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('./results/confusion_matrix.png')
#plt.show()