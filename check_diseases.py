import pandas as pd

# Load datasets
description = pd.read_csv("datasets/description.csv")
medications = pd.read_csv('datasets/medications.csv')
diets = pd.read_csv("datasets/diets.csv")
workout = pd.read_csv("datasets/workout_df.csv")
precautions = pd.read_csv("datasets/precautions_df.csv")

# Get unique diseases from each dataset
desc_diseases = set(description['Disease'].unique())
med_diseases = set(medications['Disease'].unique())
diet_diseases = set(diets['Disease'].unique())
workout_diseases = set(workout['disease'].unique())
precaution_diseases = set(precautions['Disease'].unique())

# Disease list from main.py
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer disease', 1: 'AIDS', 12: 'Diabetes', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}
model_diseases = set(diseases_list.values())

print("=== DISEASE NAME COMPARISON ===")
print(f"Description dataset: {len(desc_diseases)} diseases")
print(f"Medications dataset: {len(med_diseases)} diseases")
print(f"Diets dataset: {len(diet_diseases)} diseases")
print(f"Workout dataset: {len(workout_diseases)} diseases")
print(f"Precautions dataset: {len(precaution_diseases)} diseases")
print(f"Model predictions: {len(model_diseases)} diseases")

print("\n=== MISSING FROM DATASETS ===")
print("Diseases in model but missing from:")
print(f"Description: {model_diseases - desc_diseases}")
print(f"Medications: {model_diseases - med_diseases}")
print(f"Diets: {model_diseases - diet_diseases}")
print(f"Workout: {model_diseases - workout_diseases}")
print(f"Precautions: {model_diseases - precaution_diseases}")

print("\n=== EXACT DISEASE NAMES ===")
print("Model diseases:")
for disease in sorted(model_diseases):
    print(f"  '{disease}'")

print("\nWorkout diseases:")
for disease in sorted(workout_diseases):
    print(f"  '{disease}'")