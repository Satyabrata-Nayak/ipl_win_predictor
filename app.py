import pickle
import pandas as pd
import streamlit as st
teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Deccan Chargers', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils',
       'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
       'Rising Pune Supergiants', 'Gujarat Lions', 'Delhi Capitals',
       'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans']
venue = ['M Chinnaswamy Stadium', 'Punjab Cricket Association Stadium',
       'Feroz Shah Kotla', 'Wankhede Stadium', 'Eden Gardens',
       'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium',
       'MA Chidambaram Stadium', 'Dr DY Patil Sports Academy', 'Newlands',
       "St George's Park", 'Kingsmead', 'SuperSport Park', 'Buffalo Park',
       'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium', 'Sardar Patel Stadium',
       'Barabati Stadium', 'Vidarbha Cricket Association Stadium',
       'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium',
       'Holkar Cricket Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Maharashtra Cricket Association Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Punjab Cricket Association IS Bindra Stadium',
       'Saurashtra Cricket Association Stadium', 'Green Park',
       'M.Chinnaswamy Stadium', 'Arun Jaitley Stadium',
       'Narendra Modi Stadium', 'Zayed Cricket Stadium',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
       'Barsapara Cricket Stadium',
       'Maharaja Yadavindra Singh International Cricket Stadium']
st.title("IPL Win Predictor")

[col1,col2]=st.columns(2)
with col1:
    batting = st.selectbox("Batting team",sorted(teams))
with col2:
    bowling = st.selectbox('Bowling team',sorted(teams))
venue = st.selectbox("Match Venue",sorted(venue))
target = st.number_input("Targeted Score",step=1)
[col1,col2,col3]= st.columns(3)
with col1:
    score = st.number_input('Current Score of Batting Team',min_value=0,max_value=target)
with col2:
    overs = st.number_input("Overs Finished",min_value=1,max_value=19)
with col3:
    wickets = st.number_input("Fall of Wickets",min_value=0,max_value=9)

if st.button('Predict Probability'):
    runs_left = target-score
    wickets_left = 10 - wickets
    balls_left = 120 -6*overs
    crr = score/overs
    rrr = runs_left*6/balls_left
    query = pd.DataFrame({'target_runs':[target],'venue':[venue],'batting_team':[batting],'bowling_team':[bowling],'runs_left':[runs_left],'wickets_left':[wickets_left],'balls_left':[balls_left],'crr':[crr],'rrr':[rrr]})
    pipe = pickle.load(open('pipe.pkl','rb'))
    result = (pipe.predict_proba(query))*100
    st.header(f"{batting} winning with {round(result[0][1])}%")
    st.header(f"{bowling} winning with {round(result[0][0])}%")


