import pandas as pd
# Sample symptoms and diseases
data = {
    'Fever': [1, 0, 1, 0],
    'Cough': [1, 1, 0, 0],
    'Fatigue': [0, 1, 1, 1],
    'Headache': [1, 0, 0, 1],
    'Sore Throat': [0, 1, 1, 0],
    'Runny Nose': [1, 1, 0, 0],
    'Nausea': [0, 1, 1, 1],
    'Diarrhea': [0, 0, 1, 1],
    'Disease': ['flu', 'cold', 'food_poisoning', 'migraine']
}

df = pd.DataFrame(data)
df.to_csv('symptom_data.csv', index=False)
print("Dataset saved to symptom_data.csv")
