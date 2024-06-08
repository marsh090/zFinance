import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 5rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Attempt to read the CSV file
try:
    expenses_df = pd.read_csv('expenses.csv')
    if expenses_df.empty:
        raise ValueError("Empty CSV file")
except (FileNotFoundError, ValueError) as e:
    st.error("The CSV file is missing or empty. Please fill out the Domestic Control page.")
else:
    categories = expenses_df['Category']
    percentages = expenses_df['Percentage']
    values = expenses_df['Value']

    color1, color2, color3, color4, color5, color6 = 'C24747', 'ED8A54', 'C2B500', '1AA512', '4959E9', '8737CD'
    color_map = {
        'Fixed expenses': f'#{color1}',
        'Comfort': f'#{color2}',
        'Goals': f'#{color3}',
        'Pleasures': f'#{color4}',
        'Education': f'#{color5}',
        'Financial freedom': f'#{color6}'
    }

    fig = px.pie(expenses_df, values='Percentage', names='Category', hole=0.75, color='Category',
                 color_discrete_map=color_map)

    # Customize layout
    fig.update_layout(
        font=dict(
            family="Inter, sans-serif"
        ),
        showlegend=False
    )

    fig.update_traces(textinfo='percent', textfont_size=18, textfont_color='#ffffff')

    st.title("Dashboard")
    st.markdown('---')

    chart_title = f'### Pie chart of expenses:'
    st.markdown(chart_title)
    col1, col2 = st.columns([2, 1])

    col1.plotly_chart(fig)

    details_title = '### Expense Details:'
    col2.markdown(details_title)
    total_percentage = 0
    numbers = [1, 2, 3, 4, 5, 6]
    for category, percentage, value, number in zip(categories, percentages, values, numbers):
        col2.markdown(f"- {category}: **:green[{percentage}%]** - :green[R$ {value:.2f}]")
        total_percentage += percentage
    color = 'green' if total_percentage <= 100 else 'red'
    col2.markdown(f'#### Full percentage: :{color}[{total_percentage}%]')
    st.markdown('---')
