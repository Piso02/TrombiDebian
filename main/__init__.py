import os

from flask import Flask

from flask_wtf.csrf import CSRFProtect

current_path = os.environ['PATH']
print(current_path)

app = Flask(__name__)




app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

csrf = CSRFProtect(app)

print('Inside __init__py')

from main import app

