# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# This notebook conatins SnoMed/[NHS Dictionary of Medicines and Devices](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/) codes for combination products for hypertension.

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''WITH bnf_codes AS (
  SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
(
bnf_code LIKE '0205051G0%' OR #  Co-Zidocapt (Hydchloroth/Captopril) 
bnf_code LIKE '0205051H0%' OR #  Enalapril Maleate with Diuretic 
bnf_code LIKE '0205052A0%' OR #  Irbesartan with Diuretic 
bnf_code LIKE '0205051K0%' OR #  Lisinopril with Diuretic 
bnf_code LIKE '0205052P0%' OR #  Losartan Potassium With Diuretic 
bnf_code LIKE '0205052AC%' OR #  Olmesartan Medox/Amlodipine/Hydchloroth 
bnf_code LIKE '0205052AB%' OR #  Olmesartan Medoxomil/Amlodipine 
bnf_code LIKE '0205052Y0%' OR #  Olmesartan Medoxomil/Hydrochlorothiazide 
bnf_code LIKE '0205051Z0%' OR #  Perindopril Arginine with Diuretic 
bnf_code LIKE '0205051AC%' OR #  Perindopril + Calcium Channel Blocker 
bnf_code LIKE '0205051N0%' OR #  Perindopril Erbumine with Diuretic 
bnf_code LIKE '0205051AB%' OR #  Perindopril Tosilate/Indapamide 
bnf_code LIKE '0205051P0%' OR #  Quinapril Hydrochloride with Diuretic 
bnf_code LIKE '0205051S0%' OR #  Ramipril with Calcium Channel Blocker 
bnf_code LIKE '0205052R0%' OR #  Telmisartan with Diuretic 
bnf_code LIKE '0205051V0%' OR #  Trandolapril + Calcium Channel Blocker 
bnf_code LIKE '0205052X0%' OR #  Valsartan with Diuretic
bnf_code LIKE '0206020Z0%' OR #  Valsartan/Amlodipine 
bnf_code LIKE '0202040T0%' OR #  Spironolactone With Loop Diuretics 
bnf_code LIKE '0202040S0%' OR #  Spironolactone With Thiazides 
bnf_code LIKE '0204000Y0%' OR #  Co-Prenozide (Oxprenolol HCl/Cyclopenth) 
bnf_code LIKE '020400040%' OR #  Co-Tenidone (Atenolol/Chlortalidone) 
bnf_code LIKE '0204000U0%' OR #  Atenolol With Calcium Channel Blocker 
bnf_code LIKE '0204000F0%' OR #  Atenolol With Diuretic 
bnf_code LIKE '0204000W0%' OR #  Metoprolol Tartrate With Diuretic 
bnf_code LIKE '020400010%' OR #  Pindolol With Diuretic 
bnf_code LIKE '0204000Q0%' OR #  Propranolol Hydrochloride With Diuretic 
bnf_code LIKE '020400030%')    #  Timolol With Diuretic 
AND 
form_route LIKE '%.oral%'
)

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

combination_bp_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','combination_bp_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
combination_bp_codelist
# -




