import pandas as pd
import plotly.express as px
import plotly.io as pio
# print(pio.renderers)

confirmed = "cov19/time_series_covid19_confirmed_global.csv"
recovered = "cov19/time_series_covid19_recovered_global.csv"
deaths = "cov19/time_series_covid19_deaths_global.csv"

covid_confirmed = pd.read_csv(confirmed)
covid_recovered = pd.read_csv(recovered)
covid_dead = pd.read_csv(deaths)

# print(covid_confirmed.head())


total_confirmed =  covid_confirmed.iloc[:,-1].sum()
# print('Total Confirmed: ',total_confirmed)

# Find the last column with non-zero data for recovered cases
last_recovered_col = None
for i in range(len(covid_recovered.columns)-1, -1, -1):
    if covid_recovered.iloc[:, i].sum() > 0:
        last_recovered_col = i
        break

if last_recovered_col is not None:
    total_recovered = covid_recovered.iloc[:, last_recovered_col].sum()
    # print(f'Total Recovered (as of {covid_recovered.columns[last_recovered_col]}): {total_recovered}')
else:
    total_recovered = 0
    # print('Total Recovered: No data available')

total_dead =  covid_dead.iloc[:,-1].sum()
# print('Total Dead: ',total_dead)

total_active = total_confirmed - total_recovered - total_dead
# print('Total Active: ',total_active)




df = pd.DataFrame(data = [total_active,total_recovered,total_dead],
                        index = ['Active','Recovered','Dead'],
                        columns=['Total'])
# print(df)



# Plotly Pie Chart - Enhanced Styling
fig = px.pie(df, values='Total',
         names=df.index,
         labels=['Active Cases','Recovered','Deaths'],
         hole=0.5,  # Larger hole for donut effect
         title='COVID-19 Global Overview<br><sub>Total Cases: {:,}</sub>'.format(total_confirmed),
         color=df.index,
         color_discrete_map={
             'Active': '#e74c3c',      # Bright red
             'Recovered': '#27ae60',   # Bright green  
             'Dead': '#34495e'         # Dark gray
         })

# Text and Styling
fig.update_traces(
    textposition='inside', 
    textinfo='percent+label+value',
    textfont=dict(size=14, color='white', family='Arial Bold'),
    showlegend=True,
    insidetextorientation='horizontal',
    hovertemplate='<b>%{label}</b><br>' +
                  'Count: %{value:,.0f}<br>' +
                  'Percentage: %{percent}<br>' +
                  '<extra></extra>',
    marker=dict(
        line=dict(color='white', width=3)  # White border around segments
    )
)

# Layout
fig.update_layout(
    title=dict(
        text='COVID-19 Global Overview<br><sub>Total Cases: {:,}</sub>'.format(total_confirmed),
        x=0.5,
        y=0.95,
        font=dict(size=24, color='#2c3e50', family='Arial Black')
    ),
    font=dict(family="Arial", size=12, color="#2c3e50"),
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.02,
        font=dict(size=14, color='#2c3e50'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#bdc3c7',
        borderwidth=1
    ),
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(t=100, b=50, l=50, r=150),
    width=800,
    height=600
)

# Add annotations for better visual appeal
fig.add_annotation(
    text="COVID-19<br>Global Impact",
    x=0.5, y=0.5,
    font_size=16,
    font_color='#7f8c8d',
    showarrow=False,
    xref="paper", yref="paper"
)

# Add a subtle background color
fig.update_layout(
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='rgba(0,0,0,0)'
)
# Save as HTML file
fig.show()
fig.write_html("cov19/covid_pie_chart.html")