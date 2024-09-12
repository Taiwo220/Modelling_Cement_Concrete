from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    # Initialize result as empty to pass to the template
    result = ''
    return render_template('index.html', result=result)

@app.route("/admin")
def me():
    return("Admin is here")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        # Retrieve input data from the form
        Cement = float(request.form['Cement'])
        Blast_Furnace_Slag = float(request.form['Blast_Furnace_Slag'])
        Fly_Ash = float(request.form['Fly_Ash'])
        Water = float(request.form['Water'])
        Superplasticizer = float(request.form['Superplasticizer'])
        Coarse_Aggregate = float(request.form['Coarse_Aggregate'])
        Fine_Aggregate = float(request.form['Fine_Aggregate'])
        Age_day = float(request.form['Age_day'])

        # Make a prediction using the model
        input_data = [[Cement, Blast_Furnace_Slag, Fly_Ash, Water, 
                       Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age_day]]
        result = model.predict(input_data)[0]

        # Return the prediction result to the template
        return render_template('index.html', result=result)

    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('index.html', result="An error occurred. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
