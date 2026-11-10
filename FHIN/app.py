from load_data import load_visits
from analytics import (
    total_revenue, 
    total_visits,
    unique_customers,
    average_spend
)

visits = load_visits()

revenue = total_revenue(visits)
visit_count = total_visits(visits)
customer_count = unique_customers(visits)

print("Total Revenue:", revenue)
print("Visits:", visit_count)
print("Customers:", customer_count)

avg_spend = average_spend(visits)

print("Average Spend:", round(avg_spend, 2))