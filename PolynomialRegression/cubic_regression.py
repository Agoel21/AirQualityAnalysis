import numpy as np;
from scipy.optimize import fsolve

class CubicRegression: 
  def _init_(self):
    self.coefficients = None

  def fit(self, X, y): 
    X_cubic = np.hstack([np.ones((X.shape[0],1)), X, X**2, X**3])
    self.coefficients = np.linalg.inv(X_cubic.T.dot(X_cubic)).dot(X_cubic.T).dot(y)

  def predict(self, X):
    X_cubic = np.hstack([np.ones((X.shape[0], 1)), X, X**2, X**3])
    return X_cubic.dot(self.coefficients)
  
  def r2_score(self, y, y_pred): 
    ss_total = np.sum((y - np.mean(y))**2)
    ss_residual = np.sum((y - y_pred)**2)
    return 1 - (ss_residual / ss_total)
  