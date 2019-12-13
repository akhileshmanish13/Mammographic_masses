from flask import Flask,request,render_template
import joblib

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

def Ad_Severity(age,shape,margin,density):
    model = joblib.load('mammo_model.sav')
    predictions = model.predict([[age,shape,margin,density]])
    return predictions

@app.route("/logistic",methods = ['POST', 'GET'])
def logistic():
    if (request.method == 'POST'):
        values = request.form
        print(values)
        age = values['Age']
        shape = values['shape']
        margin = values['margin']
        density = values['density']
        age = int(age)
        shape = int(shape)
        margin = int(margin)
        density = int(density)

        Severity = Ad_Severity(age,shape,margin,density)

        data = {
            'age': age,
            'shape': shape,
            'margin': margin,
            'density':density,
            'Severity': Severity[0]
        }

        return render_template('logistic.html', data = data)




if __name__ == '__main__':
    app.run()
