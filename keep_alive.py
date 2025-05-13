from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "PhantomScalerX is running on Railway!"

def keep_alive():
    t = Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))))
    t.start()