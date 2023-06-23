# Shipping Cost Prediction using Linear Regression 💸✈️🚚🚢💲

![image](https://github.com/keerthikkn/Shipping_cost_prediction/assets/42544473/39b78678-356d-42e3-91a2-5995f29f1f7a)


This repository contains a machine learning model trained to predict shipping costs based on various features. The model utilizes the Linear Regression algorithm, a popular method for modeling the relationship between dependent and independent variables.

The purpose of this project is to provide a web application that allows users to input the relevant features and obtain an estimated shipping cost based on the trained model.

## Dataset 📂

The dataset used for training and evaluation contains historical shipping data, including features such as package dimensions, weight, source location, destination location, and shipping method. The dataset also includes the actual shipping costs for each record, which serve as the target variable for training the model.

## Exploratory Data Analysis 📊

![image](https://github.com/keerthikkn/Shipping_cost_prediction/assets/42544473/9d74128f-b1ca-406f-95f2-f0912906a792)
![image](https://github.com/keerthikkn/Shipping_cost_prediction/assets/42544473/b6a20058-51d3-4566-9fd8-bfe8c66cc368)
![image](https://github.com/keerthikkn/Shipping_cost_prediction/assets/42544473/8645dd1c-f777-4413-963f-59e8f7f9bb43)




## Model Architecture

The Linear Regression model fits a linear equation to the input features, allowing us to estimate the shipping cost based on the values of these features. The model learns the relationship between the independent variables (features) and the dependent variable (shipping cost) during the training process.

## Model Training 

The model training process involves the following steps:

1. Data preprocessing: The dataset is preprocessed by handling missing values, encoding categorical features, and normalizing numerical features as required.

2. Splitting the dataset: The dataset is split into training and testing sets to evaluate the model's performance on unseen data. A common split is 80% for training and 20% for testing.

3. Model initialization: The Linear Regression model is initialized.

4. Model training: The Linear Regression model is trained on the training set using the `fit` method. This process involves finding the optimal coefficients for the linear equation that minimizes the difference between the predicted and actual shipping costs.

5. Model evaluation: The trained model is evaluated on the testing set using evaluation metrics such as mean squared error (MSE), root mean squared error (RMSE), and R-squared score to assess its performance.

## Web Application 🖥️

A Flask web application is provided in this repository to facilitate the prediction of shipping costs based on the trained Linear Regression model.

The web application features include:

- User-friendly web interface for entering the relevant shipping details.
- Real-time prediction of shipping costs using the trained model.
- Display of the predicted shipping cost on the web page.

## Usage

To run the Shipping Cost Prediction web application:

1. Install the required dependencies mentioned in the `requirements.txt` file.

2. Ensure that you have the pre-trained Linear Regression model available. If not, you can train the model using the provided code or load a pre-trained model.

3. Start the web application by running the `app.py` file using the command `python app.py`.

4. Open your web browser and navigate to `http://localhost:5000` to access the application.

5. Enter the relevant shipping details in the input fields and click the "Predict" button.

6. The predicted shipping cost will be displayed on the web page.

## Repository Contents 🗃️

- `cost_prediction.ipynb`: Contains the implementation of the Linear Regression model architecture, training, and evaluation procedures.
- `app.py`: Includes the code for the Flask web application.
- `requirements.txt`: Lists the required dependencies for running the application.
- `Lrmodel.pkl` : pickle file of trained linear regression model.
- `scalerx.pkl` : scaled pickle file for independent attributes.
- `scalery.pkl` : scaled pickle file for dependent attribute.
- `README.md` : description about the ML model and web application.
  
## Conclusion

The provided web application demonstrates how to predict shipping costs using a pre-trained Linear Regression model. Users can input the relevant shipping details through the web interface, and the application will provide an estimated shipping cost based on the trained model.
### performance
![image](https://github.com/keerthikkn/Shipping_cost_prediction/assets/42544473/83752162-407c-428c-b38a-fef3efd3e87a)


Please refer to the source code and accompanying comments for more detailed information about the implementation and customization options for the web application.
