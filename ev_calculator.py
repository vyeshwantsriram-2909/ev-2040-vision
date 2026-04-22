# ============================================
# EV 2040 INDIA COMPLETE CALCULATOR
# Created by yewshwantssriram-2909
# Project: Reduce petrol vehicles in India by 2040
# ============================================

print("=" * 50)
print("🚗 EV 2040 INDIA CALCULATOR")
print("=" * 50)

# STEP 1: Get user information
print("\n📋 TELL US ABOUT YOURSELF")
print("-" * 30)
name = input("Your name: ")
city = input("Your city: ")
daily_km = float(input("Daily km you drive: "))
current_vehicle = input("Current vehicle (petrol/diesel): ").lower()
income = float(input("Your annual income (₹): "))

# STEP 2: Calculate fuel costs
if current_vehicle == "petrol":
    fuel_cost = 7.5
elif current_vehicle == "diesel":
    fuel_cost = 6.5
else:
    fuel_cost = 7.0

ev_cost = 1.2

# STEP 3: Calculate savings
daily_fuel = daily_km * fuel_cost
daily_ev = daily_km * ev_cost
daily_savings = daily_fuel - daily_ev

yearly_fuel = daily_fuel * 365
yearly_ev = daily_ev * 365
yearly_savings = daily_savings * 365

# STEP 4: Calculate subsidy (based on income)
if income < 500000:
    subsidy_percent = 100
    subsidy_text = "FULL SUBSIDY (100%)"
elif income < 1500000:
    subsidy_percent = 50
    subsidy_text = "50% SUBSIDY"
else:
    subsidy_percent = 25
    subsidy_text = "25% SUBSIDY"

# STEP 5: Display results
print("\n" + "=" * 50)
print(f"📊 EV REPORT FOR {name.upper()}")
print("=" * 50)

print(f"\n📍 Location: {city}")
print(f"🚗 Daily driving: {daily_km} km")
print(f"⛽ Current vehicle: {current_vehicle.upper()}")

print("\n💰 COST COMPARISON")
print("-" * 30)
print(f"Daily fuel cost: ₹{daily_fuel:.2f}")
print(f"Daily EV cost: ₹{daily_ev:.2f}")
print(f"Daily savings: ₹{daily_savings:.2f}")

print(f"\nYearly fuel cost: ₹{yearly_fuel:,.2f}")
print(f"Yearly EV cost: ₹{yearly_ev:,.2f}")
print(f"Yearly savings: ₹{yearly_savings:,.2f}")

print("\n🏷️ GOVERNMENT SUBSIDY")
print("-" * 30)
print(f"Income: ₹{income:,.0f}")
print(f"Eligibility: {subsidy_text}")

# STEP 6: 10-year projection
print("\n📈 10-YEAR SAVINGS PROJECTION")
print("-" * 30)
for year in range(1, 11):
    total_saved = yearly_savings * year
    print(f"Year {year}: ₹{total_saved:,.0f} saved")

# STEP 7: Environmental impact
co2_per_km = 0.120  # kg CO2 for petrol
co2_yearly = daily_km * 365 * co2_per_km
trees_equivalent = int(co2_yearly / 20)

print("\n🌍 ENVIRONMENTAL IMPACT")
print("-" * 30)
print(f"Yearly CO2 from your petrol vehicle: {co2_yearly:,.0f} kg")
print(f"By switching to EV, you save {co2_yearly:,.0f} kg CO2")
print(f"That's like planting {trees_equivalent} trees every year!")

# STEP 8: India's total electricity need by 2040
print("\n⚡ INDIA'S ELECTRICITY NEED BY 2040")
print("-" * 30)

total_vehicles_india = 350000000  # 35 crore vehicles by 2040
ev_percentage = 50  # Assume 50% are EV
ev_count = (total_vehicles_india * ev_percentage) / 100
avg_km = 30
electricity_per_km = 0.15

daily_electricity = ev_count * avg_km * electricity_per_km / 1000000
yearly_electricity = daily_electricity * 365

print(f"Total vehicles in India by 2040: {total_vehicles_india:,.0f}")
print(f"EVs by 2040 (50% target): {ev_count:,.0f}")
print(f"Daily electricity needed: {daily_electricity:,.0f} million kWh")
print(f"Yearly electricity needed: {yearly_electricity:,.0f} million kWh")

# STEP 9: Policy recommendation (FASTag model)
print("\n📜 MY POLICY RECOMMENDATION")
print("-" * 30)
print("🇮🇳 FASTag Model for EVs:")
print("• 2026-2030: Build infrastructure")
print("• 2031-2035: Phase out commercial petrol vehicles")
print("• 2036-2040: Complete ban on new petrol vehicles")

# STEP 10: Final verdict
print("\n" + "=" * 50)
print("✅ FINAL VERDICT")
print("=" * 50)

if yearly_savings > 50000:
    print(f"{name}, you will save ₹{yearly_savings:,.0f} EVERY YEAR!")
    print("You should buy an EV today! 🚗")
elif yearly_savings > 25000:
    print(f"{name}, you save ₹{yearly_savings:,.0f} per year.")
    print("Consider buying an EV within 2 years.")
else:
    print(f"{name}, your savings are ₹{yearly_savings:,.0f} per year.")
    print("Wait for EV prices to drop further.")

print("\n" + "=" * 50)
print("🎯 GOAL: ZERO PETROL VEHICLES BY 2040")
print("=" * 50)
print("Thank you for using EV 2040 India Calculator!")
print("Created by: yewshwantssriram-2909")
print("📱 GitHub: https://github.com/yewshwantssriram-2909/ev-2040-vision")
