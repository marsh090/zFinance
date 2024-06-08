import streamlit as st
import csv
import os

expenses = ["fixed_expenses", "comfort", "goals", "pleasures", "education", "financial_freedom"]

st.title("Domestic Control")

col2, col3 = st.columns([3, 1])
col1, _ = st.columns([5, 0.1])


def custom_format(value):
    return "" if value == 0 or value == 100 else str(value)


default_values = {
    "fixed_expenses": 50,
    "comfort": 10,
    "goals": 10,
    "pleasures": 10,
    "education": 10,
    "financial_freedom": 10,
    "income": 0
}

if os.path.exists('expenses.csv') and os.path.getsize('expenses.csv') > 0:
    with open('expenses.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            default_values[row['Category'].lower().replace(" ", "_")] = int(row['Percentage'])
            if row['Category'] == 'Fixed expenses':
                default_values['income'] = float(row['Value']) / (int(row['Percentage']) / 100)
else:
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Percentage', 'Value'])

fixed_expenses = col1.slider(r"$\textsf{\large Fixed expenses}$", 0, 100, default_values['fixed_expenses'])
fixed_expenses_value_placeholder = col1.empty()

comfort = col1.slider(r"$\textsf{\large Comfort}$", 0, 100, default_values['comfort'])
comfort_value_placeholder = col1.empty()

goals = col1.slider(r"$\textsf{\large Goals}$", 0, 100, default_values['goals'])
goals_value_placeholder = col1.empty()

pleasures = col1.slider(r"$\textsf{\large Pleasures}$", 0, 100, default_values['pleasures'])
pleasures_value_placeholder = col1.empty()

education = col1.slider(r"$\textsf{\large Education}$", 0, 100, default_values['education'])
education_value_placeholder = col1.empty()

financial_freedom = col1.slider(r"$\textsf{\large Financial freedom}$", 0, 100, default_values['financial_freedom'])
financial_freedom_value_placeholder = col1.empty()

income = col3.number_input(r"$\textsf{\large Income}$", value=default_values['income'])

total_percentage = fixed_expenses + comfort + goals + pleasures + education + financial_freedom

color = 'green' if total_percentage <= 100 else 'red'
col1txt = f"#### :{color}[{total_percentage}%] out of 100%"
col2.markdown(col1txt)

fe_value = (fixed_expenses / 100) * income
c_value = (comfort / 100) * income
g_value = (goals / 100) * income
p_value = (pleasures / 100) * income
ed_value = (education / 100) * income
ff_value = (financial_freedom / 100) * income

fixed_expenses_value_placeholder.text(f"R$ {fe_value:.2f}")
comfort_value_placeholder.text(f"R$ {c_value:.2f}")
goals_value_placeholder.text(f"R$ {g_value:.2f}")
pleasures_value_placeholder.text(f"R$ {p_value:.2f}")
education_value_placeholder.text(f"R$ {ed_value:.2f}")
financial_freedom_value_placeholder.text(f"R$ {ff_value:.2f}")

if st.button('Save'):
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Percentage', 'Value'])
        writer.writerow(['Fixed expenses', fixed_expenses, fe_value])
        writer.writerow(['Comfort', comfort, c_value])
        writer.writerow(['Goals', goals, g_value])
        writer.writerow(['Pleasures', pleasures, p_value])
        writer.writerow(['Education', education, ed_value])
        writer.writerow(['Financial freedom', financial_freedom, ff_value])
