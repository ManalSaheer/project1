import streamlit as st
import pickle
from PIL import Image 

def  main():
    st.title(":rainbow[AIRLINE SATISFACTION SURVEY]")     
    image=Image.open('img.png')
    st.image(image,width=800)
    opt=['0','1']


    id=st.text_input(":red[id]",' ')
    Gender=st.radio(":green[Gender]",opt)
    Customer_type=st.radio(":blue[Customer type]",opt)
    Age=st.text_input(":orange[Age]",' ')
    Type_of_Travel=st.radio(":red[Type of Travel]",opt)
    Flight_Distance=st.text_input(":green[Flight Distance]",' ')
    Inflight_wifi_service=st.text_input(":blue[Inflight wifi service]",' ')
    Ease_of_Online_booking=st.text_input(":orange[Ease of Online booking]",' ')
    Food_and_drink=st.text_input(":red[Food and drink]",' ')
    Seat_comfort=st.text_input(":green[Seat comfort]",' ')
    On_board_service=st.text_input(":blue[On-board service]",' ')
    Baggage_handling=st.text_input(":orange[Baggage handling]",' ')
    Checkin_service=st.text_input(":red[Checkin service]",' ')
    Inflight_service=st.text_input(":green[Inflight service]",' ')
    Cleanliness=st.text_input(":blue[Cleanliness]",' ')
    Business=st.radio(":orange[Business]",opt)
    Eco=st.radio(":red[Eco]",opt)
    Eco_plus=st.radio(":green[Eco plus]",opt)
    
    features=[id,Gender,Customer_type,Age,Type_of_Travel,Flight_Distance,Inflight_wifi_service,Ease_of_Online_booking,Food_and_drink,Seat_comfort,On_board_service,Baggage_handling,Checkin_service,Inflight_service,Cleanliness,Business,Eco,Eco_plus]


    model=pickle.load(open('dt.sav','rb'))
    scaler=pickle.load(open('sdt.sav','rb'))

    pred=st.button('PREDICT')

    if pred:
        prediction=model.predict(scaler.fit_transform([features]))

        if prediction==0:
            st.write('NOT SATISFIED')

        else:
            st.write('SATISFIED')
main()