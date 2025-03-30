import pandas as pd
import streamlit as st
#pip install yfinance (for stock price analyser -- yahoo finance(yfinance))
import yfinance as yf
import datetime


### create env with following code to run smoothly
#conda create -n stock_analyser_env python=3.9 pandas numpy streamlit conda activate stock_analyser_env"""

#NOW WEBSITE DEVELOPMENT

# for heading using "#-- markdown"
st.write(
    """
    # Stock Price Analyser
    
    """
)

# ticker_symbol = "AAPL" 

# No HARDCODING BUT USING INPUT FROM USER
ticker_symbol = st.text_input(
                                "Input The Ticker Symbol",
                                "AAPL",
                                key = "placeholder"
)

ticker_data = yf.Ticker(ticker_symbol)


# Using Column Layout To Display Start Date and End Date In One Row
col1, col2 = st.columns(2)

with col1:
    sd = st.date_input("Input Start Date", value = None) # Use only this line of code for sinle line input

with col2:
    ed = st.date_input("Input End Date", value = None)

# Note : IN PLACE OF StartDate AND EndDate MANUALLY DATE CAN ALSO BE HARDCODED  YYYY-MM-DD
ticker_df = ticker_data.history(
    period = "1d",
    start = sd,
    end = ed
)

# Representing The Data Into DataFrame
st.write(f"""
        ### The Stock prices of {ticker_symbol}
""")
st.dataframe(ticker_df)


# VISUALISATION 
st.write("""
    ##  Daily Closing Price Chart
        """
         )
st.line_chart(ticker_df.Close)

st.write("""
     ##  Volume Of Shares Traded
        """
         )
st.line_chart(ticker_df.Volume)
