from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('symptom_model.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

symptoms = ['Fever', 'Cough', 'Fatigue', 'Headache', 'Sore Throat', 'Runny Nose', 'Nausea', 'Diarrhea']

# Detailed info for diseases
disease_info = {
    "Common Cold": {
        "description": "A viral infection of your nose and throat. It’s usually harmless.",
        "precautions": [
            "Drink warm fluids like soup or tea",
            "Get plenty of rest",
            "Avoid cold and dusty environments"
        ],
        "feel_better": [
            "Use saline nasal spray",
            "Take steam inhalation twice a day",
            "Stay hydrated and eat nutritious food"
        ]
    },
    "Flu": {
        "description": "Influenza (flu) is a viral infection that attacks your respiratory system.",
        "precautions": [
            "Stay home and avoid spreading it to others",
            "Wash hands frequently",
            "Wear a mask when around others"
        ],
        "feel_better": [
            "Take antivirals if prescribed",
            "Drink plenty of water and warm fluids",
            "Rest well and avoid stress"
        ]
    },
    "Malaria": {
        "description": "A mosquito-borne infectious disease affecting humans and animals caused by parasitic protozoans.",
        "precautions": [
            "Sleep under mosquito nets",
            "Use insect repellent",
            "Avoid stagnant water around you"
        ],
        "feel_better": [
            "Take anti-malarial medication on time",
            "Stay in a cool room to avoid fever spikes",
            "Keep your body hydrated and eat light meals"
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [1 if request.form.get(symptom) == 'on' else 0 for symptom in symptoms]
    prediction = model.predict([input_data])[0]
    predicted_disease = le.inverse_transform([prediction])[0]
    return redirect(url_for('disease_info_page', disease_name=predicted_disease))

@app.route('/disease/<disease_name>')
def disease_info_page(disease_name):
    info = disease_info.get(disease_name, {
        "description": "Sorry, we don't have detailed info about this disease.",
        "precautions": ["Consult a doctor"],
        "feel_better": ["Take proper rest"]
    })
    return render_template('disease.html', disease_name=disease_name, info=info)

if __name__ == '__main__':
    app.run(debug=True)
