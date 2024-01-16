import streamlit as st
import csv
import csv


def render_signup_form(session_state):
    form_data = {}
    form_data['name'] = st.text_input('Name', value=session_state.get('name', ''))
    form_data['email'] = st.text_input('Email', value=session_state.get('email', ''))
    form_data['username'] = st.text_input('Username', value=session_state.get('username', ''))
    form_data['password'] = st.text_input('Password', value=session_state.get('password', ''), type='password')
    form_data['confirm_password'] = st.text_input('Confirm Password', value=session_state.get('confirm_password', ''), type='password')
    return form_data

def render_login_form(session_state):
    form_data = {}
    form_data['email'] = st.text_input('Email', value=session_state.get('email', ''))
    form_data['password'] = st.text_input('Password', value=session_state.get('password', ''), type='password')
    return form_data

 
def process_signup_form(form_data):
    if form_data['password'] != form_data['confirm_password']:
        st.error('Password does not match the confirm password.')
        return False
    
    if '@' not in form_data['email']:
        st.error('Email is invalid.')
        return False
    
    if write_to_csv(form_data):
        st.success(f"Welcome {form_data['name']}!")
        return True 
    
    return True

def process_login_form(form_data):
    print("Processing login form")
    #check the email is present in the csv file, if not throw an error
    with open('./user_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)  <  5:
                continue
            if row[1] == form_data['email'] and row[3] == form_data['password']:
                st.success(f"Welcome {row[0]}!")
                print("MATCHED !!!!!!")
                return True
    return False

def write_to_csv(form_data):
    #check if the email is already present in the csv file, if yes throw an error
    with open('./user_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)  <  5:
                continue
            if row[1] == form_data['email']:
                st.error(f"Email {form_data['email']} already exists.")
                return False
            
    with open('./user_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([form_data['name'], form_data['email'], form_data['username'], form_data['password'], form_data['plan']])
        print("Wrote to CSV")
        return True
    return False