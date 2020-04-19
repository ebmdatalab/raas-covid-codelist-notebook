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

# The following notebook contains medicines that are [ACE Inhibitors from the RAS section](https://openprescribing.net/bnf/020505/) of BNF codes. All cobination products have been excluded and the list has been cross refereneced with [the actual BNF for "Other drugs in the class ace inhibitors"](https://bnf.nice.org.uk/drug/ramipril.html#indicationsAndDoses).

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''WITH bnf_codes AS (
  SELECT bnf_code FROM hscic.presentation WHERE 
(bnf_code LIKE '0205051F0%' OR #    Captopril 
bnf_code LIKE '0205051E0%' OR #  Cilazapril 
bnf_code LIKE '0205051I0%' OR #  Enalapril Maleate 
bnf_code LIKE '0205051J0%' OR #  Fosinopril Sodium 
bnf_code LIKE '0205051W0%' OR #  Imidapril Hydrochloride 
bnf_code LIKE '0205051L0%' OR #  Lisinopril 
bnf_code LIKE '0205051Y0%' OR #  Perindopril Arginine 
bnf_code LIKE '0205051M0%' OR #  Perindopril Erbumine 
bnf_code LIKE '0205051AA%' OR #  Perindopril Tosilate 
bnf_code LIKE '0205051Q0%' OR #  Quinapril Hydrochloride 
bnf_code LIKE '0205051R0%' OR #  Ramipril 
bnf_code LIKE '0205051U0%' )  #  Trandolapril 

  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

acei_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','acei_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
acei_codelist
# -

# ## Lisinopril
# In the study we are possibly going to ook at indivodual agents which may have a effect. Below sets out a codelist for lisinopril

lisinopril_codelist = acei_codelist.loc[acei_codelist["bnf_code"].str.contains('0205051L0')]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
lisinopril_codelist.to_csv(os.path.join('..','data','lisinopril_codelist.csv')) #export to csv here
lisinopril_codelist

