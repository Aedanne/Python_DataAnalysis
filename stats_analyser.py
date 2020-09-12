import numpy as np

def calculate(alist):

  if len(alist) < 9:
    raise ValueError('List must contain nine numbers.')

  a = np.array(alist).reshape(3,3)

  mean_list = [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a.flatten())]
  var_list = [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a.flatten())] 
  std_list = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a.flatten())] 
  max_list = [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a.flatten())] 
  min_list = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a.flatten())] 
  sum_list = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a.flatten())] 

  calculations = dict()
  calculations['mean'] = mean_list
  calculations['variance'] = var_list
  calculations['standard deviation'] = std_list
  calculations['max'] = max_list
  calculations['min'] = min_list
  calculations['sum'] = sum_list

  return calculations
