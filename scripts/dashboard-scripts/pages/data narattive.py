import streamlit as st 
import pandas as pd
import plotly.express as px

st.title("Fuel & Energy Overview: Global to Regional Perspectives")

df = pd.read_csv("Energy.csv")
df.replace(".","",inplace=True)

with st.expander("Data Preview"):
    st.dataframe(df,column_config={"Year" : st.column_config.NumberColumn(format="%d")})
    
st.header("Globally")
st.subheader('Total Energy', divider='rainbow')


st.info('This is a purely informational message', icon="ℹ️")

#st.write(f'You wrote {len(txt)} characters.')

# TEP YEAR 2022
continents = ["Africa","Latin America","Europe","Middle-East","North America","Asia","Pacific"]
df_cont = df[(df["Countries"].isin(continents)) & (df["Year"]==2022)]
df_cont = df_cont[["Countries","TEP"]]
values_1 = df_cont["TEP"].values
labels_1 = df_cont["Countries"].values

# TEP YEAR 2000
df_cont = df[(df["Countries"].isin(continents)) & (df["Year"]==2012)]
df_cont = df_cont[["Countries","TEP"]]
values_2 = df_cont["TEP"].values
labels_2 = df_cont["Countries"].values

col1,col2 = st.columns(2)


with col2 :
    fig1= px.treemap(values_1 , path=[labels_1],values=values_1,title ="Total Eneregy Production 2022")
    st.plotly_chart(fig1, use_container_width=True)


with col1 :
    fig2= px.treemap(values_2 , path=[labels_2],values=values_2,title ="Total Energy Production 2012")
    st.plotly_chart(fig2, use_container_width=True)


#TEC 2022 
df_cont = df[(df["Countries"].isin(continents)) & (df["Year"]==2022)]
df_cont = df_cont[["Countries","TEC"]]
values_1 = df_cont["TEC"].values
labels_1 = df_cont["Countries"].values   

#TEC 2000 
df_cont = df[(df["Countries"].isin(continents)) & (df["Year"]==2012)]
df_cont = df_cont[["Countries","TEC"]]
values_2 = df_cont["TEC"].values
labels_2 = df_cont["Countries"].values   


with col2 :
    fig1= px.treemap(values_1 , path=[labels_1],values=values_1,title ="Total Eneregy Consumption 2022")
    st.plotly_chart(fig1, use_container_width=True)


with col1 :
    fig2= px.treemap(values_2 , path=[labels_2],values=values_2,title ="Total Energy Consumption 2012")
    st.plotly_chart(fig2, use_container_width=True)


st.header("Organisationly")
st.subheader('Crude Oil', divider='rainbow')
st.info('This is a purely informational message', icon="ℹ️")

colu1,colu2 = st.columns(2)
df_oil = df[["COP","Orgs","Year","COBT"]]
condition_1 = df_oil["Year"].isin([2013,2016,2019,2022])
condition_2 = ~df["Orgs"].isin(["Other"])
df_oil = df_oil[(condition_1)&(condition_2)]
df_oil['Year'] = df_oil['Year'].astype(str)
df_oilp = df_oil.groupby(["Orgs","Year"])["COP"].sum().to_frame().reset_index()
df_oil['Year'] = df_oil['Year'].astype(str)



with colu1 : 
    fig = px.bar(df_oilp,x="Orgs",y="COP",color="Year")
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)

    
with colu2 : 
    fig = px.bar(df_oil,x="Orgs",y="COBT",color="Year")
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)

st.header("Regionaly")

st.subheader('Coal & Lignite', divider='rainbow')
st.info('This is a purely informational message', icon="ℹ️")


countries = ["United Kingdom","France","Germany","Italy","Russia","Ukraine"]
df_count = df[df["Countries"].isin(countries)]


col1,col2 = st.columns(2)

with col1:
    fig = px.line(df_count,x="Year",y="CP",color="Countries")
    fig.update_layout(yaxis_title="Coal Production")
    st.plotly_chart(fig, use_container_width=True)


with col2:
    fig = px.line(df_count,x="Year",y="CC",color="Countries")
    fig.update_layout(yaxis_title="Coal Consumption")
    st.plotly_chart(fig, use_container_width=True)


selected = ["European Union","Russia","Ukraine"]
condition_1 = df["Countries"].isin(selected)
condition_2 = ~df["Year"].isin([2022])
war_df = df[(condition_1)&(condition_2)] 
war_df2 = df[(condition_1)&(~condition_2)] 





st.subheader('Natural Gas', divider='rainbow')
st.info('This is a purely informational message', icon="ℹ️")


# Create two buttons horizontally
tab1, tab2 = st.tabs(["Before War", "During War"])

with tab1 : 
    col1,col2 = st.columns(2)
    with col1 : 
        fig2 = px.pie(war_df, values="GP", names="Countries", hole=.3,title="Total Natural Gas Production")
        st.plotly_chart(fig2, use_container_width=True)
    with col2 : 
        fig2 = px.pie(war_df, values="GC", names="Countries", hole=.3,title="Total Natural Gas Consumption")
        st.plotly_chart(fig2, use_container_width=True)

with tab2 : 
    col3,col4 = st.columns(2)
    with col3 : 
        fig3 = px.pie(war_df2, values="GP", names="Countries", hole=.3,title="Total Natural Gas Production")
        st.plotly_chart(fig3, use_container_width=True)
    with col4 : 
        fig3 = px.pie(war_df2, values="GC", names="Countries", hole=.3,title="Total Natural Gas Consumption")
        st.plotly_chart(fig3, use_container_width=True)   


