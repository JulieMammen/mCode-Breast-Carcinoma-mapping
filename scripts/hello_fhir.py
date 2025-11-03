# scripts/hello_fhir.py
from fhir.resources.patient import Patient
import json, os
from dotenv import load_dotenv

load_dotenv()

print("UMLS key loaded:", "Yes" if os.getenv("UMLS_API_KEY") else "No")

patient = Patient.construct(
    id="example-001",
    name=[{"text": "Jane Doe"}]
)

print("\n--- FHIR Patient JSON ---")
print(json.dumps(patient.dict(), indent=2))
