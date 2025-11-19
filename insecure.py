# Examples of insecure code that Bandit will flag

def connect_to_database():
    password = "MySecretPassword123"  
    return f"postgresql://user:{password}@localhost/db"


def run_user_code(user_input):
    exec(user_input)        # rm -rf /
    
    
def get_user(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  
    cursor.execute(query)
    return cursor.fetchone()

import pickle

def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)  
    return data


import random

def generate_token():
    token = random.randint(1000, 9999) 
    return token


import os

def ping_host(hostname):
    os.system(f"ping -c 1 {hostname}")  

import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  
    
    
def check_admin(user):
    assert user.is_admin  


from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
    
def risky_operation():
    try:
        dangerous_function()
    except: 
        pass
