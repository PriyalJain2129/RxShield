import csv
import os
from database import db_execute

def import_patients():
    # Ensure we are looking for the file in the same directory as this script
    csv_path = os.path.join(os.path.dirname(__file__), 'real_drug_dataset_updated.csv')
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: Could not find {csv_path}")
        return

    print("Reading CSV and uploading to Neon... please wait.")
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            query = """
                INSERT INTO patients (
                    patient_id, age, gender, condition, current_drug, 
                    dosage_mg, allergy_class, max_safe_dose_mg, 
                    interacts_with, clinical_warning
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (patient_id) DO UPDATE SET
                    age = EXCLUDED.age,
                    condition = EXCLUDED.condition,
                    current_drug = EXCLUDED.current_drug;
            """
            params = (
                row['Patient_ID'], int(row['Age']), row['Gender'], row['Condition'], 
                row['Drug_Name'], int(row['Dosage_mg']), row['Allergy_Class'], 
                int(row['Max_Safe_Dose_mg']), row['Interacts_With'], row['Clinical_Warning']
            )
            db_execute(query, params, is_select=False)
            count += 1
            if count % 100 == 0:
                print(f"Uploaded {count} rows...")

    print(f"✅ Success! {count} Patients imported successfully!")

if __name__ == "__main__":
    import_patients()