# Fish Market Flask App

This is a Flask web application that predicts fish species based on input data. It utilizes a machine learning model trained on fish data.

## Project Structure

- **Static folder**: Contains static assets used by the web application.
  - `style.css`: CSS stylesheets.
  - `script.js`: JavaScript code.
  - *Other media files if any*.

- **Templates folder**: Contains HTML templates defining the structure and content of web pages.
  - `index.html`: Form for accepting input to identify fish species.

- `app.py`: Core logic of the Flask web application. Defines routes, handles requests, performs predictions using the loaded model (`fish_pred_model.pkl`), and returns responses in JSON format.

- `fish_pred_model.pkl`: Pickled machine learning model object, likely containing a Linear Regression model trained on fish data.

- **Notebook folder**: Contains Jupyter Notebook `fish_market_pred.ipynb` with code for dataset analysis and linear regression prediction model.

## Usage

1. Clone the repository: 
    
`git clone https://github.com/nikhil2297/Fish-Market-Flask-App.git`


2. Navigate to the project directory:

`cd Fish-Market-Flask-App`


3. Install dependencies:

`pip install -r requirements.txt`


4. Run the Flask application:

`python app.py`


5. Open a web browser and go to `http://localhost:5000` to access the application.

## Live Demo

You can access the live demo of this application [here](https://fishmarket-flask-app-40e994df9b85.herokuapp.com/).

## Contributors

- [Nikhil](https://github.com/nikhil2297)
