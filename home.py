import pandas as pd
import plotly.graph_objs as go
import pickle

import streamlit as st
st.set_page_config(layout="wide")
def display_aqi_prediction_page():
   
    st.markdown(
    """
    <style>
        /* Set background image */
        .stApp {
            background-image: url('https://lp-cms-production.imgix.net/2019-06/b8c99d401b90bd06021c122b4346c8f7-maiden-s-tower.jpg');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
    st.title("Air Quality Index Prediction for Baku")

    col1, col2 = st.columns(2)

    # Read and preprocess data
    df = pd.read_csv('baku_aqi.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    daily_aqi = df['aqi'].resample('D').mean().reset_index()

    # Function to create a smoothed trend line
    def create_smoothed_trace(df, window=21):
        smoothed_aqi = df['aqi'].rolling(window=window, center=True, min_periods=1).mean()
        return go.Scatter(
            x=df['timestamp'], 
            y=smoothed_aqi, 
            mode='lines',
            name='Smoothed Trend',
            line=dict(color='red', width=2)
        )

    # Function to create a detailed AQI plot
    def create_clean_aqi_plot(daily_aqi, forecast_df):
        daily_aqi_last_15 = daily_aqi.tail(15)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily_aqi_last_15['timestamp'], 
            y=daily_aqi_last_15['aqi'],
            mode='lines+markers',
            name='Daily AQI',
            line=dict(color='#1E90FF', width=3),
            marker=dict(size=8, color='#1E90FF', symbol='circle', line=dict(width=2, color='white')),
            hovertemplate='<b>Date</b>: %{x}<br><b>AQI</b>: %{y:.2f}<extra></extra>'
        ))
        
         # Add color-coded zones based on AQI levels
        fig.add_hrect(y0=0, y1=50, 
                    annotation_text='Good', 
                    annotation_position='left',
                    fillcolor='green', 
                    opacity=0.1,
                    layer='below')
        
        fig.add_hrect(y0=50, y1=100, 
                    annotation_text='Moderate', 
                    annotation_position='left',
                    fillcolor='yellow', 
                    opacity=0.1,
                    layer='below')
        
        fig.add_hrect(y0=100, y1=150, 
                    annotation_text='Unhealthy', 
                    annotation_position='left',
                    fillcolor='orange', 
                    opacity=0.1,
                    layer='below')
        
        fig.add_hrect(y0=150, y1=200, 
                    annotation_text='Very Unhealthy', 
                    annotation_position='left',
                    fillcolor='red', 
                    opacity=0.1,
                    layer='below')
    

     # Rest of the function remains the same...
      

        fig.add_trace(go.Scatter(
            x=forecast_df.index, 
            y=forecast_df['Forecast'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='orange', width=3),
            marker=dict(size=8, color='orange', symbol='circle', line=dict(width=2, color='white')),
            hovertemplate='<b>Date</b>: %{x}<br><b>Forecast AQI</b>: %{y:.2f}<extra></extra>'
        ))

        fig.update_layout(
            title={'text': 'Air Quality Index - Last 15 Days', 'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
            xaxis_title='Date',
            yaxis_title='Air Quality Index',
            template='plotly_white',
            height=450,
            width=800,
            hovermode='closest',
        )
        return fig

    # Create original trace
    original_trace = go.Scatter(
        x=daily_aqi['timestamp'], 
        y=daily_aqi['aqi'], 
        mode='lines',
        name='Daily AQI',
        line=dict(color='blue', width=1.5),
        opacity=0.2
    )
    smoothed_trace = create_smoothed_trace(daily_aqi)

    # Combine traces in a figure
    fig = go.Figure(data=[original_trace, smoothed_trace])
    fig.update_layout(title='Daily Average AQI for Baku', yaxis_title='Average AQI', title_x=0.5, template='plotly_white')

    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("") 
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        loaded_df = pickle.load(open('predictions_for_three_days.pkl', 'rb'))
        clean_fig = create_clean_aqi_plot(daily_aqi, loaded_df)
        st.plotly_chart(clean_fig, use_container_width=True)
