
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:\\Users\\Zaid Hussain\\OneDrive\\Desktop\\Multiple_D\\Multiple_D\\trained_model.sav', 'rb'))

heart_model = pickle.load(open('C:\\Users\\Zaid Hussain\\OneDrive\\Desktop\\Multiple_D\\Multiple_D\\heartdis_model.sav', 'rb'))




with st.sidebar:
    
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['activity','heart-fill'],
                           
                           default_index = 0)
    

if(selected == 'Diabetes Prediction'):

    
    st.title('Diabetes Prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
          Glucose = st.text_input('Glucose Level')
    with col3:
          BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
         SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
         Insulin = st.text_input('Insulin Level')
    with col3:
         BMI = st.text_input('BMI Value')
    with col1:
         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    
    
    if st.button('Diabetes Test Result'):
        diab_Prediction = diabetes_model.predict([[ Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,  BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_Prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
        
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
        st.success(diab_diagnosis)                   
    
    
if(selected == 'Heart Disease Prediction'):
        
        
        st.title('Heart Disease Prediction using ML')
        
        col1,col2,col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
        with col2:
             sex = st.text_input('Sex')
        with col3:
             cp = st.text_input('Chest Pain Types')
        with col1:
             trestbps = st.text_input('Resting Blood Pressure')
        with col2:
             chol = st.text_input('Serum Cholestrol in mg/dL')
        with col3:
             fbs = st.text_input('Fasting Blood sugar > 120 mg/dL')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
             ca = st.text_input('Major vessels colored by fluorosopy')
        with col1:
             thal = st.text_input('thal: 0 = normal; 1 = fiixed defect; 2 = reverseable defect')
             
             heart_diagnosis = ''
             
             
             
             if st.button('Heart Disease Test Result'):
                 heart_Prediction = heart_model.predict([[ age, sex, cp, trestbps, chol,  fbs, restecg, thalach,  exang, oldpeak, slope,  ca, thal]])
                 
                 if(heart_Prediction[0]==1):
                     heart_diagnosis = 'The Person is having Heart Disease'
                 
                 else:
                     heart_diagnosis = 'The Person does not have any Heart Disease'
                 st.success(heart_diagnosis) 
               
        
        
        
