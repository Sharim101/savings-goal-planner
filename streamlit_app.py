import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Savings Goal Planner", page_icon="💰")

# Title
st.title("💰 Savings Goal Planner")
st.markdown("Plan your financial goals and track your savings progress!")

# Sidebar Inputs
st.sidebar.header("Enter Your Details")
goal_amount = st.sidebar.number_input("Target Savings Goal ($)", min_value=100, value=10000)
current_savings = st.sidebar.number_input("Current Savings ($)", min_value=0, value=1000)
time_period = st.sidebar.number_input("Time Period (Years)", min_value=1, max_value=50, value=5)
annual_return = st.sidebar.number_input("Expected Annual Return (%)", min_value=0.0, max_value=20.0, value=5.0) / 100

# Calculate Monthly Savings Needed
months = time_period * 12
future_value = goal_amount - current_savings * (1 + annual_return) ** time_period
monthly_savings = (future_value * annual_return / 12) / ((1 + annual_return / 12) ** months - 1)

# Display Results
st.subheader("📊 Savings Plan Summary")
col1, col2 = st.columns(2)
col1.metric("Monthly Savings Needed", f"${monthly_savings:,.2f}")
col2.metric("Total Savings in {time_period} Years", f"${goal_amount:,.2f}")

# Projected Growth Table
st.subheader("📈 Projected Growth Over Time")
years = list(range(1, time_period + 1))
savings_growth = []
for year in years:
    savings_growth.append(current_savings * (1 + annual_return) ** year + monthly_savings * 12 * year)

data = pd.DataFrame({
    "Year": years,
    "Savings": savings_growth
})

st.dataframe(data)

# Plot Growth Chart
fig, ax = plt.subplots()
ax.plot(data["Year"], data["Savings"], marker="o")
ax.set_xlabel("Years")
ax.set_ylabel("Savings ($)")
ax.set_title("Projected Savings Growth")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("### How It Works:")
st.write("""
1. Enter your **target savings goal**, **current savings**, and **time period**.
2. Adjust the expected **annual return rate** (e.g., 5% for conservative investments).
3. The app calculates how much you need to save **each month**.
4. View a table and chart of your projected savings growth.
""")
