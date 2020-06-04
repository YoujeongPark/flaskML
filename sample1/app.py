from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

# import joblib

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/predict', methods=['POST'])
def predict():
    # df = pd.read_csv("data/names_dataset.csv")
    # # Features and Labels
    # df_X = df.name
    #
    # # Vectorization
    # corpus = df_X
    # cv = CountVectorizer()
    # X = cv.fit_transform(corpus)

    # Loading our ML Model
    regression_model = open("data/pickleIRIS.pkl", "rb")
    clf = joblib.load(regression_model)

    # Receives the input query from form
    if request.method == 'POST':
        v1 = float(request.form['v1'])
        v2 = float(request.form['v2'])
        v3 = float(request.form['v3'])
        v4 = float(request.form['v4'])
        data = np.array([v1,v2,v3,v4])
        data = data.reshape(1,-1)
        my_prediction = clf.predict(data)
        print(my_prediction)
    return render_template('results.html', prediction=my_prediction )
    #name=namequery.upper()

if __name__ == '__main__':
    app.run(port="7878", debug=True)