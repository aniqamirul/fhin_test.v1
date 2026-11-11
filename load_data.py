import pandas as pd

def load_visits():
    visits = pd.read_excel(
        "fhinautospa.aniqsdatabase.xlsx",
        sheet_name="Fhin V1 (Visits Sheet)"
    )
    return visits

def load_customers():
    customers = pd.read_excel(
        "fhinautospa.aniqsdatabase.xlsx",
        sheet_name="Fhin V1 (Customer Sheet)"
    )
    return customers