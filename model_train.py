import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv('symptom_data.csv')

# Encode disease labels
le = LabelEncoder()
df['Disease'] = le.fit_transform(df['Disease'])

# Save encoder
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

# Train the model
X = df.drop('Disease', axis=1)
y = df['Disease']

model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open('symptom_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved.")
