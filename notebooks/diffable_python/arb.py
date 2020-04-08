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

# The following notebook contains medicines that are [Angiotensin II receptor antagonists from the RAS section](https://openprescribing.net/bnf/020505/) of BNF codes. All cobination products have been excluded and the list has been cross refereneced with [the actual BNF for "Other drugs in the class ace inhibitors"](https://bnf.nice.org.uk/drug/candesartan-cilexetil.html#indicationsAndDoses).

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''WITH bnf_codes AS (
  SELECT bnf_code FROM hscic.presentation WHERE 
(bnf_code LIKE '0205052AD%' OR #  Azilsartan Medoxomil
bnf_code LIKE '0205052C0%' OR #  Candesartan Cilexetil
bnf_code LIKE '0205052W0%' OR #  Eprosartan 
bnf_code LIKE '0205052I0%' OR #  Irbesartan
bnf_code LIKE '0205052N0%' OR #  Losartan Potassium
bnf_code LIKE '0205052B0%' OR #  Olmesartan Medoxomil
bnf_code LIKE '0205052Q0%' OR #  Telmisartan 
bnf_code LIKE '0205052V0%')    #  Valsartan
)

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

arb_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','arb_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
arb_codelist
