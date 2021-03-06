!pip install tweet-preprocessor

import numpy as np
import pandas as pd
import re

def preprocessor(dataFile):
  
  f = open(dataFile, "r")
  preprocessed_Data = []
  result1 = ''
  result2 = ''
  result3 = ''

  for x in f:
    result1 = x.split('|')[2] 
    result2 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",result1).split())

    if result2.startswith('RT'):
      result2 = result2.replace('RT ','').lower()
      preprocessed_Data.append(result2)
    else:
      preprocessed_Data.append(result2.lower())

  raw_input = pd.DataFrame(preprocessed_Data) 

  f.close()

  print(raw_input)
  return raw_input


def k_means(raw_input, k=5, max_iter=100):

  centroids = []

  count = 0

  while count < k:
    cent = rd.randint(0,len(raw_input) -1)
  return clusters, sse

def jaccard(a, b):
  intersect = list(set(a) & set(b))
  inter = len(intersect)

  union = list(set(a) | set(b))
  uni = len(union)

  return round(1-(float(inter) / uni), 4)

def main():
  #preprocessing data
  dataFile = '/content/usnewshealth.txt'
  data = preprocessor(dataFile)

  updates = 3
  k = 5

  for u in range(updates):
    print("k means # " + str(u+1))

    clusters, sse = k_means(raw_input, k)

  #print size in each clusers; useful for the table

    for c in range (len(clusters)):
      print(str(c+1) + ": ", str(len(clusters[c])) + " tweets")

    print("SSE : " + STR(sse) + "\n")
    k+=1


if __name__ == "__main__":
  main()


#SSE
def sse(cluster, centroids, terms_all, k, l):
    indices1 = []
    indices = [id.index(item) for item in centroids]
    cen_txt = [terms_all[x] for x in indices]
    sum = 0
    for i in range(k):
        indices1.append([j for j, u in enumerate(cluster) if u == i])
        # print indices1[i]
        t = [terms_all[x] for x in indices1[i]]
        for j in range(len(indices1[i])):
            sum = sum + math.pow(jaccard(t[j], cen_txt[i]), 2)
    print('SSE', sum, file=f)
