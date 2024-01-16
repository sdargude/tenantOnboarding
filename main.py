import streamlit as st
import csv
from helper import render_signup_form,render_login_form,process_signup_form,process_login_form


# Set page title and favicon.
st.set_page_config(page_title="My Webpage", page_icon="🏃‍♀️🏃‍♀️🏃‍♀️🏃‍♀️....", layout="wide")

 
st.subheader("SwiftSummarizer: Your Shortcut to PDF Mastery!",)
st.write(
        "#### Empowering efficient knowledge extraction through cutting-edge technology with SwiftSummarizer, simplifying the way you interact with PDFs."
        )

st.write("---")

 
# Initialize session state if it doesn't exist
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
if 'plan' not in st.session_state:
    st.session_state['plan'] = ''
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'email' not in st.session_state:
    st.session_state['email'] = ''
if 'Username'  not in st.session_state:
    st.session_state['Username'] = ''
if 'Password' not in st.session_state:
    st.session_state['Password'] = ''

    
 
# Home page
if st.session_state['page'] == 'home':
    leftcol, rightcol  = st.columns(2)

    with leftcol:
       
        st.write("#### Unleash the power of SwiftSummarizer, the game-changer in PDF processing! Seamlessly transform complex documents into concise, 20-line summaries, tailored for professionals, students, and researchers. Experience efficiency like never before – SwiftSummarizer simplifies information overload, empowering you to make informed decisions faster. Say goodbye to lengthy reading and hello to instant insights. Elevate your productivity with SwiftSummarizer – download now for a smarter approach to PDFs!")

    with rightcol:
        with st.form(key='login_form',): 
            form_data = render_login_form(st.session_state)
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button('Log In'):
                    # Process the login form 
                    print(form_data)
                    if process_login_form(form_data):
                        print(form_data)
                        st.session_state.update(form_data)
                        st.session_state['page'] = 'login_successful'
                        st.write(form_data)
                    else:
                        st.session_state['page'] = 'login_failed'

                    st.rerun()
            with col2:
                if st.form_submit_button('Cancel'):
                    # Process the cancel action
                    # This will depend on your specific application
                    st.session_state['page'] = 'home'
                    st.session_state['email'] = ''
                    st.session_state['Password'] = ''
                    st.rerun()    
    st.write("---")

    bronze_column, silver_column, gold_column = st.columns(3)
    with bronze_column:
        st.header("Bronze") 
        #use relative path
        st.image("./images/howtostoredocuments.webp")
        st.write("""
            This is the bronze package. It has the following features:
            - Upload your PDF document to SwiftSummarizer. You can either drag and drop your file or click on the upload button.
            - Enter your email address. We will send you a link to your summary as soon as it is ready.
            - Receive your summary via email. You can also download your summary directly from the app.
        """)
        if st.button('Try it', key='bronze_button'):
            st.session_state['plan'] = 'Bronze'
            st.session_state['page'] = 'form'
            st.rerun()
            

    with silver_column:
        st.header("Silver") 
        st.image("./images/howtostoredocuments.webp")
        st.write("""
            This is the Silver package. It has the following features:
            - Upload your PDF document to SwiftSummarizer. You can either drag and drop your file or click on the upload button.
            - Enter your email address. We will send you a link to your summary as soon as it is ready.
            - Receive your summary via email. You can also download your summary directly from the app.
        """)
     
        if st.button('Try it', key='silver_button'):
            st.session_state['plan'] = 'Silver'
            st.session_state['page'] = 'form'
            st.rerun()

    with gold_column:
        st.header("Gold") 
        st.image("./images/howtostoredocuments.webp")
        st.write("""
            This is the Gold package. It has the following features:
            - Upload your PDF document to SwiftSummarizer. You can either drag and drop your file or click on the upload button.
            - Enter your email address. We will send you a link to your summary as soon as it is ready.
            - Receive your summary via email. You can also download your summary directly from the app.
        """)
        if st.button('Try it', key='gold_button'):
            st.session_state['plan'] = 'Gold'
            st.session_state['page'] = 'form'
            st.rerun()
    st.write("---")

# Form page 
elif st.session_state['page'] == 'form':
    st.write('You selected the ',st.session_state['plan'],'plan!')
    with st.form(key='my_form'):
        st.write('Please sign up or log in.')
         


      
        form_data = render_signup_form(st.session_state)
        form_data['plan'] = st.session_state['plan']
    

        if st.form_submit_button('Submit'):
            if process_signup_form(form_data):
                st.write('Sign up successful.')
                st.session_state.update(form_data)
                st.session_state['page'] = 'summary'
                st.rerun()
        
            else:
                st.error("Please fill out all the fields before submitting.")
        
# Summary page
elif st.session_state['page'] == 'summary':
    st.write(f"Name: {st.session_state['name']}")
    st.write(f"Email: {st.session_state['email']}")
    st.write(f"Plan: {st.session_state['plan']}")
    st.balloons()

elif st.session_state['page'] == 'login_successful':
    st.write("Login Successful")
    st.balloons()

elif st.session_state['page'] == 'login_failed':
    st.write("###Login Failed!!")
    st.snow()

