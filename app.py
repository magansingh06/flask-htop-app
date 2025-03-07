from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Magan Singh"
    username = os.getlogin()
    server_time = "07-03-2025 14:50 IST"
    
    # Run top command and capture the first 10 lines
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
