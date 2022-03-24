
from flask import Flask
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    #a = np.array([1, 3])
    #b = np.array([3, 5])
    #plt.plot(a,b)
    return 'Hello World'

if __name__ == '__main__':
    app.run()
