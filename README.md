# mCODE-Breast-Carcinoma-mapping
## BreastCancer-FHIR Profiler
### mCode: Mapping Breast Cancer Data to FHIR Breast cancer is one of the deadliest diseases out there, but good data standards-like FHIR-can help. This repo shows how to take raw, messy infiltrating ductal carcinoma records, clean them, convert ICD-10 codes to SNOMED using UMLS API, and bundle 'em up into FHIR resources.  ###
### How to run it
1. Clone: git clone https://github.com/JulieMammen/mCode.git
2. Install: pip install -r requirements.txt[requests for UMLS pulls, pandas for profiling, fhir.resources for building bundles, .env]
3. Try sample: python mapping_api.py data/idc_dummy_data.csv
###
## 🧭 Git & VS Code Workflow

This section describes how to work with this project using **Git**, **GitHub**, and **VS Code**.

### 🪄 1️⃣ Clone the Repository

Open your terminal (or VS Code terminal):

```powershell
git clone https://github.com/JulieMammen/mCode-Breast-Carcinoma-mapping.git
cd mCode-Breast-Carcinoma-mapping
