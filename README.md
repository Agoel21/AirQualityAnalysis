# Air Quality Analysis

This project analyzes various pollutant data using Polynomial regression, Exponential Regression, and Simpson's Method. 

Presentation video link: https://www.youtube.com/watch?v=yVF_1T74Hq4 

## Description
### Exponential Regression
Implementation of the algorithm in ExponentialRegression/exponentialRegression.ipynb along with all the metrics. Relevant graph images are saved within the folder.

### Polynomial Regression
Implementation of all three (Linear, Quadratic, Cubic) in the PolynomialRegression folder through main.py. All the metrics are generated through analysis.py.

### Simpson's method
Implementation of the algorithm in Simpsonsmethod folder along with all the metrics. Relevant graph images are saved within the folder.

Follow the steps below to set up and run the program on the CSCE server.

## Common Execution steps 

### 1. Download and Extract the Files

run the following commands to extract the ZIP:

```bash
unzip AirQualityAnalysis.zip -d AirQualityAnalysis
cd AirQualityAnalysis
```

### 2. Create a virtual environment 
```bash 
python3 -m venv env
source env/bin/activate
```

### 3. Install pip 
```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

### 4. Install necessary libraries from requirements.txt 
```bash
python3 -m pip install -r requirements.txt
```

## Polynomial Regression Execution steps

### 5. cd into the Polynomial Regression directory
```bash
cd PolynomialRegression
```

### 6. Run the program
```bash
python3 main.py
```

### 7. To compare the ($R^2$) score and Computational Complexity for the different polynomial degrees
```bash 
python3 analysis.py
```

## Exponential Regression and Simpson's Method exeution steps

### 5. Run Jupyter Notebook on the Server
```bash
jupyter notebook --no-browser --port=8888
```

### 6. Forward the Port to Your Local Machine (can jump to step 7 step if running on personal computer and CSCE server)
```bash
ssh -L 8888:localhost:8888 your_username@university_server_address
```

### 7. Access the Notebook
Open the notebook on the browser using: 
Copy and paste the link shown on the server terminal 
or 
go to "http://localhost:8888" and copy and paste the token from the Jupyter Notebook output (shown on the server terminal)


### 8. Run the Notebook
Navigate to the ExponentialRegression and SimpsonsMethod directory in the Jupyter interface and open the .ipynb file. Run all cells.

### Simpler method to run without CSCE server: Upload the notebooks and csv file to Google Colab or Jupyter Notebooks to run them.

### Note: All the results already visible in the .ipynb files for Exponential Regression and Simpson's Method
