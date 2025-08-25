from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
app = Flask(__name__)

#load the model names
model_names = ['LinearRegression', 'RidgeRegression', 'LassoRegression', 'ElasticNetRegression',
               'PolynomialRegression', 'SGDRegressor', 'ANN', 'Random Forest',
                'SupportVectorRegressor', 'K-NearestNeighbors', 'XGBoost', 'LightGBM(lgbm)'
                
]

models = {name:pickle.load(open('model.pkl', 'rb'))  for name, model in model_names}

# Load evaluation results
results_df = pd.read_csv(r"D:\Naresh IT foundation\NIT_Python\model_results.csv")

@app.route('/')
def index():
    return render_template('index.html',model_names=model_names)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
   model_names=request.form['model']
   input_data = {
       'Avg. Area Income': float(request.form['Avg_Area_Income']),
       'Avg. Area House Age': float(request.form['Avg_Area_House_Age']),
       'Avg. Area Number of Rooms': float(request.form['Avg_Area_Number_of_Rooms']),
       'Avg. Area Number of Bedrooms': float(request.form['Avg_Area_Number_of_Bedrooms']),
       'Area Population': float(request.form['Area_Population'])
   }
   input_df = pd.DataFrame([input_data])
   if model_names in models:
       model=model_names[model_names]
       prediction=model.predict(input_df)[0]
       return render_template('result.html', model_name=model_names, prediction=prediction)
   else:
       return jsonify({'error': 'Model not found'}), 404   

@app.route('/results')
def results():
    return render_template('model.html', tables=[results_df.to_html(classes='data')], titles=results_df.columns.values)
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app on port 5000
# Note: Ensure that the model.pkl and model_evaluation_results.csv files are in the same        
       