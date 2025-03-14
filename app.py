from flask import Flask

app = Flask(__name__)

#from dashboard import *
from home import *
from chatIa import *



import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""      # Força o uso apenas da CPU
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"       # Reduz os avisos de nível INFO e WARNING
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"  # Corrige erro de incompatibilidade

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render define a porta automaticamente
    app.run(host="0.0.0.0", port=port, debug=False)
