import random
import pandas as pd

# Updated list of diagnoses
diagnoses = [
    'Diabetes', 'Hypertension', 'Asthma', 'Obesity', 'Anxiety',
    'Coronary Heart Disease', 'Breast Cancer', 'Prostate Cancer',
    'Alzheimer\'s Disease', 'Osteoarthritis', 'Migraine', 'Epilepsy',
    'Psoriasis', 'Rheumatoid Arthritis', 'Peptic Ulcer', 'Hypothyroidism',
    'Hyperthyroidism', 'Pneumonia', 'Tuberculosis', 'Dermatitis'
]

# Updated list of treatments
treatments = [
    'Medication', 'Lifestyle Changes', 'Surgery', 'Inhalers',
    'Diet and Exercise', 'Psychotherapy', 'Radiation Therapy',
    'Physical Therapy', 'Bypass Surgery', 'Insulin Therapy', 'Chemotherapy',
    'Antibiotics', 'Vaccination', 'Hormone Replacement', 'Immunotherapy',
    'Counseling', 'Acupuncture', 'Chiropractic Care', 'Blood Transfusion',
    'Dialysis'
]

# Function to generate random data with the updated lists
def generate_random_data_extended(num_rows):
    data = []
    for _ in range(num_rows):
        patient_id = random.randint(1000, 9999)
        age = random.randint(18, 85)
        gender = random.choice(['M', 'F'])
        diagnosis = random.choice(diagnoses)
        treatment = random.choice(treatments)
        outcome = random.choice(['Improved', 'Stable', 'Declined', 'Remission'])
        data.append([patient_id, age, gender, diagnosis, treatment, outcome])
    return pd.DataFrame(data, columns=['Patient ID', 'Age', 'Gender', 'Diagnosis', 'Treatment', 'Outcome'])

# Generate 50 rows of sample data with the extended lists
extended_sample_data = generate_random_data_extended(50)
print(extended_sample_data.head(10))  # Display the first 10 rows
extended_sample_data.to_csv("sample.csv", sep=',', index=False)
