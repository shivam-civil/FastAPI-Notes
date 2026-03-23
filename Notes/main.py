# NOTES WHILE LEARNING FASTAPI 

# 1 : VIRTUAL ENVIRONMENT 
'''

pip -m venv myenv  # This creates myenv folder .
./myenv/Scripts/activate  # This activates the virtual environment.

'''

# 2 : USE OF FASTAPI CLASS FROM fastapi module 
'''
from fastapi import FastAPI
app = FastAPI()  # DONT FORGET THE SPACE BETWEEN THE "=". ERROR 1 RAISED.
'''

# 3 : RUN THE FASTAPI SCRIPT 
'''
fastapi dev main.py
'''
 
# 4 : SEND DATAS TO ENDPOINTS 
'''
@app.get("/")   # Default Endpoint : https://127.0.0.0:80000
def homepage():
   return "Welcome to HomePage"

@app.get("/dashboard")  # Dashboard Page EndPoint
def dashboard():
   return "Welcome to Dashboard"   
'''