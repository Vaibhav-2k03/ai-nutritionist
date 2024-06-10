import streamlit as st
from streamlit_lottie import st_lottie
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import json
import os

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

def diet_plan_generator(age,height,weight,gender,health_issues,eating_preference):

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    template ="""
    You are a great dietitian who is food and nutrition expert and 
    provides medical nutrition therapy and counseling for particular individuals.
    Give a Proper Balanced diet chart for a person having following details:
    Age : {age} years
    Height: {height} cm
    Weight: {weight} kg
    Gender: {gender}
    Health Issues: {health_issues}
    Eating Preferences: {eating_preference}

    Provide Diet is a proper format for breakfast, lunch, dinner and so on with timings,calories,etc.
    Also Mention the BMI of the person at the begining of diet chart and also mention expected calories intake prefered for the day.
    Mention if there is any proper precautions to be maintained by the person.  
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({
        "age":age,
        "height":height,
        "weight":weight,
        "gender":gender,
        "health_issues":health_issues,
        "eating_preference": eating_preference
    })

def load_lottiefile(filepath: str):
    with open(filepath, 'r',encoding="utf8") as f:
        return json.load(f)

st.set_page_config(page_icon='🤖',page_title='AI Nutritionist',layout='wide')
title_writing = "AI Nutritionist 🛡️🧑🏻‍⚕️🛡️"
title_format = f'<p style="text-align: center; font-family: ' \
                f'Arial; color: black; font-size: 40px; ' \
                f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)

with col2:
        load = load_lottiefile('lottiefiles/Diet_gif.json')
        st_lottie(load,quality='high',speed='2')
        

# st.title('Diet Consultant 🛡️🧑🏻‍⚕️🛡️')
st.subheader('Enter Personal Details...')
age = st.text_input('Enter Age (***years***)')
weight = st.text_input('Enter Weight (***kg***)')
height = st.text_input('Enter Height (***cm***)')
gender = st.selectbox('Select Gender',('Male','Female','Others'),index=0)
health_issues = st.text_input('**Health issuses** if any')
eating_preference = st.selectbox('Eating Preferences',('Vegetarian','Non-Vegetarian','Vegan'),index=0)


if st.button('Generate Diet',type='primary'):
    with st.spinner('*Generating your Diet...*'):
        st.success(diet_plan_generator(age,height,weight,gender,health_issues,eating_preference))




st.markdown("*Application developed by **Vaibhav V** ©*")