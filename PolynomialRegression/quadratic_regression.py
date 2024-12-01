import numpy as np;

class QuadraticRegression: 
  def _init_(self):
    self.coefficients = None

  def fit(self, X, y): 
    X_quad = np.hstack([np.ones((X.shape[0],1)), X, X**2])
    self.coefficients = np.linalg.inv(X_quad.T.dot(X_quad)).dot(X_quad.T).dot(y)

  def predict(self, X):
    X_quad = np.hstack([np.ones((X.shape[0], 1)), X, X**2])
    return X_quad.dot(self.coefficients)
  
  def r2_score(self, y, y_pred): 
    ss_total = np.sum((y - np.mean(y))**2)
    ss_residual = np.sum((y - y_pred)**2)
    return 1 - (ss_residual / ss_total)
  
  
