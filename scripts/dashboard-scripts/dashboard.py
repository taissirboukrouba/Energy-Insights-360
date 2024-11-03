import streamlit as st
import pandas as pd 
import plotly.express as px
import squarify
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# setting the layout to be wide by default 
st.set_page_config(layout="wide")
st.sidebar.header("User Profile")

profile_picture = "pfp.png"  # Replace with the path to your image
st.sidebar.image(profile_picture, width=150)  # Adjust width as needed

# Optional: Add user information or links in the sidebar
st.sidebar.write("**Username:** Jane Doe")
st.sidebar.write("**Role:** Data Scientist")
st.sidebar.write("**Location:** San Francisco, CA")



st.title("EU Fuel Statistics Dashboard")



#reading data 
df = pd.read_csv("Energy.csv")
df.replace(".","",inplace=True)


col1,col2 = st.columns(2)


# Average Annual Balance Of Trade (Natural Gas)
# Formula : Sum of balance of trades for each year / number of years
 
df_eu = df[df["Countries"]=="European Union"]
sum_gbt = df_eu["GBT"].sum()
years_count = 2022-1990 
aabt = sum_gbt/years_count



with col2 : 
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = int(aabt),
    title = {'text': "Average Annual BOT (Natural Gas)"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [-500, 500]},
    'bar': {'color': 'rgba(255,0,0,0.6)'},  # Red color
    'steps': [ {'range': [0, 500], 'color': 'rgba(255,0,0,0.6)'},
                {'range': [-500, 0], 'color': 'rgba(0,128,0,0.6)'}]}))
    st.plotly_chart(fig, use_container_width=True)
#--------------------------------------------------------------------
#Load Factor:
#Formula: (Average Energy Consumption / Maximum Energy Consumption) * 100

df_eu = df[df["Countries"]=="Europe"]
average_ener_cons = df_eu["TEC"].mean()
max_ener_cons = df_eu["TEC"].max()
load_factor = (average_ener_cons/max_ener_cons)*100

with col1 : 
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = int(load_factor),
    title = {'text': "Load Factor"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [0, 100]},
    'bar': {'color': 'rgba(255,0,0,0.6)'},  # Red color
    'steps': [ {'range': [50, 100], 'color': 'rgba(255,0,0,0.6)'},
                {'range': [0, 50], 'color': 'rgba(0,128,0,0.6)'}]}))
    st.plotly_chart(fig, use_container_width=True)


organisations = ["BRICS","G7","OECD"]





# Eneregy Production Vs Consumption Discrepancy

def eneregy_discrepancy(df,production,consumption) :
    df_20 = df[df["Year"]==2020]
    df_21 = df[df["Year"]==2021]

    discrepency_20 = df_20[production] - df_20[consumption]
    discrepency_21 = df_21[production] - df_21[consumption]

    return discrepency_20.iloc[0],discrepency_21.iloc[0]

coal_disp_20,coal_disp_21 = eneregy_discrepancy(df_eu,"CP","CC")
gas_disp_20,gas_disp_21 = eneregy_discrepancy(df_eu,"GP","GC")
oil_disp_20,oil_disp_21 = eneregy_discrepancy(df_eu,"OP","OC")



col1,col2,col3 = st.columns(3)
with col1 : 
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = coal_disp_21,
    domain = {'x': [0,1], 'y': [0, 1]},
    delta = {'reference': (coal_disp_20), 'relative': True, 'position' : "bottom",'increasing': {'color': "red"},
            'decreasing': {'color': "green"}},
    title = "Coal Discrepancy 2020-2021"))
    st.plotly_chart(fig, use_container_width=True)

with col2 : 
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = gas_disp_21,
    domain = {'x': [0,1], 'y': [0, 1]},
    title = "Gas Discrepancy 2020-2021",
    delta = {'reference': (gas_disp_20),
            'relative': True,
            'position' : "bottom",
            'increasing': {'color': "red"},
            'decreasing': {'color': "green"}}))
    st.plotly_chart(fig, use_container_width=True)

with col3 : 
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = oil_disp_21,
    domain = {'x': [0,1], 'y': [0, 1]},
    delta = {'reference': (oil_disp_20), 'relative': True, 'position' : "bottom" , 'increasing': {'color': "green"},
            'decreasing': {'color': "red"}},
    title = "Oil Discrepancy 2020-2021"))
    st.plotly_chart(fig, use_container_width=True)



#--------------------------------------------------------
#Energy (Coal)Independence Ratio  
#Formula : (Energy Production - Energy Consumption) / Energy Production

def energy_independance(start_year,end_year,country,col1,col2) : 
    condition_1 = df["Countries"]== country
    condition_2 = df["Year"]==end_year
    condition_3 = df["Year"]==start_year
    df_eu = df[condition_1]
    df_eu1 = df[(condition_1) & (condition_2)]
    df_eu2 = df[(condition_1) & (condition_3)]

    #computations : 
    df_eu = (df_eu[col1] - df_eu[col2]) / df_eu[col1]
    df_eu1 = (int(df_eu1[col1]) - int(df_eu1[col2])) / int(df_eu1[col1])
    df_eu2 = (int(df_eu2[col1]) - int(df_eu2[col2])) / int(df_eu2[col1])
    eir = df_eu1 *100
    peir = df_eu2*100
    scatt_vals = df_eu.values
    return eir,peir,scatt_vals


gas_eir,gas_peir,gas_scatt = energy_independance(2000,2022,"Europe","GP","GC")
#--------------------------------------------------------
#Crude Oil Trade Intensity Ratio   
#Formula : (Crude Oil Exports - Crude Oil Imports) / Crude Oil Production = Crude Oil Balance of Trade / Crude Oil Production


def trade_intensity_ratio (country,col1,col2) : 
    condition_1 = df["Year"].isin([2022])
    condition_2 = df["Year"].isin([2021])
    condition_3 = df["Countries"]== country
    df_trade  = df[condition_3]
    df_trade_1 = df[(condition_1)&(condition_3)]
    df_trade_2 = df[(condition_2)&(condition_3)]

    tir = df_trade[col1] / df_trade[col2]
    tir1 = df_trade_1[col1] / df_trade_1[col2]
    tir2 = df_trade_2[col1] / df_trade_2[col2]

    return tir.values,tir1,tir2

crude_oil_tir,crude_oil_tir22, crude_oil_tir21 = trade_intensity_ratio("Europe","COBT","COP")
col1,col2 = st.columns(2)

with col1: 
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = int(crude_oil_tir22),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': int(crude_oil_tir21), 'relative': True, 'position' : "bottom",'increasing': {'color': "red"},
            'decreasing': {'color': "green"}},
    title = "Crude Oil Intencity of Trade"))
    fig.add_trace(go.Scatter(y=crude_oil_tir ,line=dict(color='red', width=2)))
    st.plotly_chart(fig, use_container_width=True)
# Create a gauge chart
with col2: 
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = int(gas_eir),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': (gas_peir), 'relative': True, 'position' : "bottom",'increasing': {'color': "red"},
            'decreasing': {'color': "red"}},
    title = "Gas Independence Ratio"))
    fig.add_trace(go.Scatter(y=gas_scatt,line=dict(color='red', width=2)))
    st.plotly_chart(fig, use_container_width=True)
    

def eneregy_contribution (df,col1,col2,col3,col4,year) : 

    # defining columns :
    condition_1 = df["Year"].isin([year])
    condition_2 = df["Countries"]== "Europe"
    df = df[(condition_1)&(condition_2)]
    col1 = df[col1]
    col2 = df[col2]
    col3 = df[col3]
    col4 = df[col4]


    # defining conversions : 
    twh_to_joules = 3.6e12 
    bcm_to_joules = 1e12  
    oil_to_joules = 6.1178632e12  
    coal_to_joules = 2.93076e13  
    
    #converting values : 
    col1 = col1 * twh_to_joules 
    col2 = col2 * bcm_to_joules
    col3 = col3 * oil_to_joules
    col4 = col4 * coal_to_joules

    cols = [col1,col2,col3,col4]
    contributions = []


    #calculating total energy : 
    total_ener = col1 + col2 + col3 + col4 

    # calculating contributions : 
    for col in cols : 
        value = (col/total_ener)*100
        contributions.append(value.values[0])
        
    return contributions


contributions_22 = eneregy_contribution(df,"EP","GP","COP","CP",2022)
contributions_00 = eneregy_contribution(df,"EP","GP","COP","CP",2000)
labels=["Electricity","Natural Gas",'Crude Oil',"Coal"]



with col1:
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=contributions_00, pull=[0, 0, 0.2, 0])])
    fig2.update_layout(
        title="Energy Contributions by Source 2000",  # Title for the first pie chart
        width=800,  # Set the desired width for the chart
        height=600  # Set the desired height for the chart
    )
    st.plotly_chart(fig2, use_container_width=True)

# Create the second pie chart in the second column
with col2:
    fig1 = go.Figure(data=[go.Pie(labels=labels, values=contributions_22, pull=[0, 0, 0.2, 0])])
    fig1.update_layout(
        title="Energy Contributions by Source 2022",  # Title for the second pie chart
        width=800,  # Set the desired width for the chart
        height=600  # Set the desired height for the chart
    )
    st.plotly_chart(fig1, use_container_width=True)


