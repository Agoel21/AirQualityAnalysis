# Air Quality Analysis

This project analyzes various pollutant data using Polynomial regression, Exponential Regression, and Simpson's Method. 

Follow the steps below to set up and run the program.


## Polynomial Regression Execution Guide

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
