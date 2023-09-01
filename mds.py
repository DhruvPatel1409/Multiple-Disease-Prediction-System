import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/ADMIN/Desktop/vs code/streamlit/multiple disease prediction/saved models/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/ADMIN/Desktop/vs code/streamlit/multiple disease prediction/saved models/heart_model.sav','rb'))

parkinson_model = pickle.load(open('C:/Users/ADMIN/Desktop/vs code/streamlit/multiple disease prediction/saved models/parkinson_model.sav','rb'))

with st.sidebar:
    selected = option_menu('MULTIPLE DISEASE PREDICTION SYSTEM',
                           ['DIABETES PREDICTION','HEART DISEASE PREDICTION','PARKINSON DISEASE PREDICTION'],icons = ['activity','heart','person'] , default_index = 0)
    
# Diabetes Prediction System

if(selected == 'DIABETES PREDICTION'):

    # page title
    st.title('DIABETES PREDICTION SYSTEM')

    Pregnancies = st.number_input('Number of pregnancies : ')
    Glucose = st.number_input('Glucose Level : ')
    BloodPressure = st.number_input('Blood Pressure Value : ')
    SkinThickness = st.number_input('Skin Thickness Value : ')
    Insulin = st.number_input('Insulin Value : ')
    bmi = st.number_input('BMI Value : ')
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value  : ')
    Age = st.number_input('Enter your Age : ')

    diab_diagnosis = ' '

    if st.button('PREDICT'):
        diab_prediction = diabetes_model.predict([[Pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , bmi , DiabetesPedigreeFunction , Age]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The Person is not Diabetic"

    st.success(diab_diagnosis)

if(selected == 'HEART DISEASE PREDICTION'):

    # page title
    st.title('HEART DISEASE PREDICTION SYSTEM')

    age = st.number_input("Enter your age : ")
    sex = st.selectbox("Select Gender",("Male","Female"))
    if(sex == "Male"):
        s = 0
    if(sex == "Female"):
        s = 1
    cp = st.number_input("Enter chest pain type : ")
    trestbps = st.number_input("Enter your blood pressure : ")
    chol = st.number_input("Enter your cholestrol level : ")
    fbs = st.number_input("Enter your blood sugar level : ")
    restecg = st.number_input("Enter your ECG level : ")
    thalach = st.number_input("Enter your thalach level : ")
    exang = st.number_input("Enter your exercise angina : ")
    oldpeak = st.number_input("Enter your ST depression : ")
    slope = st.number_input("Enter your slope of ST segment : ")
    ca = st.number_input("Enter your number of major vessels : ")
    thal = st.number_input("Enter your thal level : ")

    heart_diagnosis = ''
    if st.button('PREDICT'):
        heart_prediction = heart_model.predict([[age, s, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0]==1):
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The Person is not having heart disease"

    st.success(heart_diagnosis)


if(selected == 'PARKINSON DISEASE PREDICTION'):

    # page title
    st.title('PARKINSON DISEASE PREDICTION SYSTEM')

    Fo = st.number_input("Enter your Average vocal fundamental frequency : ")
    Fhi = st.number_input("Enter your Maximum vocal fundamental frequency : ")
    Flo = st.number_input("Enter your  Minimum vocal fundamental frequency : ")
    Jitter_per = st.number_input("Enter your MDVP_Jitter(%) : ")
    Jitter_abs = st.number_input("Enter your MDVP_Jitter(Abs) : ")
    RAP = st.number_input("Enter your MDVP_RAP : ")
    PPQ = st.number_input("Enter your MDVP_PPQ : ")
    DDP = st.number_input("Enter your Jitter_DDP : ")
    Shimmer = st.number_input("Enter your MDVP_Shimmer : ")
    Shimmer_db = st.number_input("Enter your MDVP_Shimmer(dB) : ")
    APQ3 = st.number_input("Enter your Shimmer_APQ3 : ")
    APQ5 = st.number_input("Enter your Shimmer_APQ5 : ")
    APQ = st.number_input("Enter your MDVP_APQ : ")
    DDA = st.number_input("Enter your  Shimmer_DDA  : ")
    NHR = st.number_input("Enter your NHR : ")
    HNR = st.number_input("Enter your HNR : ")
    RPDE = st.number_input("Enter your RPDE : ")
    DFA = st.number_input("Enter your DFA : ")
    spread1 = st.number_input("Enter your spread1 : ")
    spread2 = st.number_input("Enter your spread2 : ")
    D2 = st.number_input("Enter your D2 : ")
    PPE = st.number_input("Enter your PPE : ")

    parkinson_diagnosis = ''

    if st.button('PREDICT'):
        parkinson_prediction = parkinson_model.predict([[Fo,Fhi,Flo,Jitter_per,Jitter_abs,RAP,PPQ,DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if (parkinson_prediction[0]==1):
            parkinson_diagnosis = "The person is having parkinson disease"
        else:
            parkinson_diagnosis = "The Person is not having parkinson disease"

    st.success(parkinson_diagnosis)


