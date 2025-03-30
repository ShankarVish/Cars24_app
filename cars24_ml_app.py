import pandas as pd
import streamlit as st
import pickle
import sklearn 

df = pd.read_csv("cars24-car-price.csv")


st.write("""
        # CARS24 Used Car Price Prediction
         
         #### Sample Dataset
""")

st.dataframe(df.head())

# we dont want user to input every feature thus we just define some feature for them to change -- by using dictionary
encode_values={
  "fuel_type":  {"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5  },
  "seller_type": {"Dealer":1,"Individual":2,"Trustmark Dealer":3     },
  "transmission_type": {"Manual":1,"Automatic":2  }
}

# Load the saved pickle file as "rb-- for read mode" and predict suing .predict method
def model_pred(fuel_type, transmission_type,engine, seats):

    # LOADING THE MODEL
    with open('car_pred', 'rb') as file:
        reg_model = pickle.load(file)

        # defualt values are given so that the user dont has to input every value though these can be changed in codes that follow  if the user wants to play with every feature
    new_X=[[2018.0, 1,  40000,   fuel_type, transmission_type, 19.70,  engine, 86.30,  seats]]
    return(reg_model.predict(new_X))


# LAYOUT OF THE WEBPAGE


st.write("""
        #### Enter The Value Of The Features For Prediction
""")
col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Choose The Fuel Type", 
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"],
                            index=None,
                            placeholder="Fuel Type")

engine = col1.slider("Slide To Select Value Of Engine",
                               500,5000,step=100)

transmission_type = col2.selectbox("Choose The Transmission Type", 
                           ["Manual", "Automatic"],
                            index=None,
                            placeholder="Transmission Type")

seats = col2.selectbox("Choose The Total Seats", 
                           [1,2,3,4],
                            index=None)

# to invoke "model_pred" function when predict button is pressed

if(st.button("Predict Price")):

    # use the encode dict to give values to model_pred 
    fuel_type=encode_values["fuel_type"][fuel_type]
    transmission_type=encode_values["transmission_type"][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("The Predicted Price Of The Car Is : " + str(price))



