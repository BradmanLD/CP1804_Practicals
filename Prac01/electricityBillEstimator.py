print("Electricity Bill Estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_33 = 0.136928
used_tariff = int(input("Which tariff? 11 or 33?: "))
if used_tariff == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_33
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Number of billing days: "))
bill_cost_dollars = cents_per_kwh * daily_use_kwh * number_of_billing_days
print("Estimated bill: $" + str(round(bill_cost_dollars, 2)))