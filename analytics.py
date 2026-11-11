def total_revenue(visits_df):
    return visits_df["Amount"].sum()


def total_customers(customers_df):
    return len(customers_df)


def repeat_customers(customers_df):
    return len(
        customers_df[
            customers_df["Customer Category"] != "New"
        ]
    )
def total_revenue(df):
    return df["Amount"].sum()

def total_visits(df):
    return len(df)

def unique_customers(df):
    return df["Clean Plate"].nunique()

def average_spend(df):
    return df["Amount"].mean()