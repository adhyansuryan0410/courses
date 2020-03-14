import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'s':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [4,7]

'''
[[plt.scatter(j[0], j[1], s=100, color='r') for j in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1])
plt.show()
'''

def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k:
    warnings.warn('k is set to a value less than the total voting groups!')
  distances = []
  for group in data:
    for features in data[group]:
      euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
      distances.append([euclidean_distance, group])

  votes = [i[1] for i in sorted(distances)[:k]]
  print(Counter(votes).most_common(1))
  vote_result = Counter(votes).most_common(1)[0][0]

  return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)