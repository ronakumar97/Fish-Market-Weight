from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        species = request.form.get('species')
        length1 = request.form.get('length1')
        length2 = request.form.get('length2')
        length3 = request.form.get('length3')
        height = request.form.get('height')
        width = request.form.get('width')

        with open('./model.pkl', 'rb') as f:
            reg = pickle.load(f)

        X = [[species, length1, length2, length3, height, width]]

        prediction = reg.predict(X)

        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
