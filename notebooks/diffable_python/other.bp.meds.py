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

# This notebook conatins medicines classed as "other antihypertensives". From [NICE CKS Hypertension guidelines](https://cks.nice.org.uk/hypertension-not-diabetic#!prescribingInfo) we will include
#
#
# - [thiazide-type diuretics](#thiazide)  --->  [Current prescribing](https://openprescribing.net/bnf/020201/)
# - [calcium channel blockers](#calcium)  --->  [Current prescribing](https://openprescribing.net/bnf/020602/)
# - [spironolactone](#spiro)              --->  [Current prescribing](https://openprescribing.net/chemical/0202030S0/)
# - [beta-blockers](#bblock)              --->  [Current prescribing](https://openprescribing.net/bnf/0204/)
# - [alpha-blockers](#ablock)             --->  [Current prescribing](https://openprescribing.net/bnf/020504/)

from ebmdatalab import bq
import os
import pandas as pd

# ## Calcium Chanel Blockers <a id='calcium'></a>

# +
sql = '''WITH bnf_codes AS (
  SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
(bnf_code LIKE '0206020A0%' OR #  Amlodipine
bnf_code LIKE '0206020C0%' OR #  Diltiazem Hydrochloride
bnf_code LIKE '0206020F0%' OR #  Felodipine
bnf_code LIKE '0206020I0%' OR #  Isradipine
bnf_code LIKE '0206020K0%' OR #  Lacidipine
bnf_code LIKE '0206020L0%' OR #  Lercanidipine Hydrochloride
bnf_code LIKE '0206020Q0%' OR #  Nicardipine Hydrochloride
bnf_code LIKE '0206020R0%' OR #  Nifedipine
bnf_code LIKE '0206020M0%' OR #  Nimodipine
bnf_code LIKE '0206020W0%' OR #  Nisoldipine
bnf_code LIKE '0206020B0%' OR #  Trimetazidine Hydrochloride
bnf_code LIKE '0206020T0%')    #  Verapamil Hydrochloride 
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

ca_blockers_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','ca_blockers_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
ca_blockers_codelist



# -

# ## Spironolactone <a id='spiro'></a>

# +
sql = '''WITH bnf_codes AS (
    SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
bnf_code LIKE '0202030S0%'  #  Spironolactone
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

spironolactone_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','spironolactone_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
spironolactone_codelist
# -

# ## Thiazide-type diuretics <a id='thiazide'></a>

# +
sql = '''WITH bnf_codes AS (
    SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
(bnf_code LIKE '0202010B0%' OR #  Bendroflumethiazide
bnf_code LIKE '0202010D0%' OR #  Chlorothiazide
bnf_code LIKE '0202010F0%' OR #  Chlortalidone
bnf_code LIKE '0202010J0%' OR #  Cyclopenthiazide
bnf_code LIKE '0202010L0%' OR #  Hydrochlorothiazide
bnf_code LIKE '0202010P0%' OR #  Indapamide
bnf_code LIKE '0202010V0%' OR #  Metolazone 
bnf_code LIKE '0202010X0%' OR #  Polythiazide
bnf_code LIKE '0202010Y0%')    #  Xipamide
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

thiazide_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','thiazide_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
thiazide_codelist
# -

# ## Beta-blockers <a id='bblock'></a>

# +
sql = '''WITH bnf_codes AS (
    SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
(bnf_code LIKE '0204000C0%' OR # Acebutolol Hydrochloride
bnf_code LIKE '0204000E0%' OR #  Atenolol
bnf_code LIKE '0204000H0%' OR #  Bisoprolol Fumarate
bnf_code LIKE '0204000AC%' OR #  Bisoprolol Fumarate/ASPIRIN
bnf_code LIKE '020400080%' OR #  Carvedilol
bnf_code LIKE '020400060%' OR #  Celiprolol Hydrochloride 
bnf_code LIKE '0204000I0%' OR #  Labetalol Hydrochloride
bnf_code LIKE '0204000K0%' OR #  Metoprolol Tartrate
bnf_code LIKE '0204000M0%' OR #  Nadolol
bnf_code LIKE '0204000AB%' OR #  Nebivolol
bnf_code LIKE '0204000N0%' OR #  Oxprenolol Hydrochloride
bnf_code LIKE '0204000P0%' OR #  Pindolol
bnf_code LIKE '0204000R0%' OR #  Propranolol Hydrochloride
bnf_code LIKE '0204000T0%' OR #  Sotalol Hydrochloride
bnf_code LIKE '0206020B0%' OR #  Trimetazidine Hydrochloride
bnf_code LIKE '0204000V0%')   # Timolol - oral
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

beta_blockers_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','beta_blockers_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
beta_blockers_codelist
# -

# ## Alpha Blockers <a id='ablock'></a>

# +
sql = '''WITH bnf_codes AS (
  SELECT DISTINCT bnf_code FROM measures.dmd_objs_with_form_route WHERE 
(bnf_code LIKE '0205040D0%' OR #  Doxazosin Mesilate
bnf_code LIKE '0205040I0%' OR #  Indoramin
bnf_code LIKE '0205040M0%' OR #  Phenoxybenzamine Hydrochloride
bnf_code LIKE '0205040P0%' OR #  Phentolamine Mesilate
bnf_code LIKE '0205040S0%' OR #  Prazosin Hydrochloride
bnf_code LIKE '0205040V0%')    #  Terazosin Hydrochloride 
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

alpha_blockers_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','alpha_blockers_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
alpha_blockers_codelist 
