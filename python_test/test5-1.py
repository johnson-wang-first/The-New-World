import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from collections import Counter


n_clusters = 5
phone_name = "OPPO"
colnames = ['NN', 'TIME', 'LANGUAGE', 'COUNTRY', 'OPERATOR', 'WEB', 'RATE1', 'RATE2', 'REVIEW', 'NAME', 'CELLPHONE']
phone_review = pd.read_csv('/Users/wzhao/Documents/processed_file.csv', names=colnames, header=None, encoding="latin_1", dtype='object')
#phone_review.dropna(inplace=True)
#phone_review.to_csv('/Users/wzhao/Documents/processed_file.csv', index=False)
Lenovo = phone_review[phone_review['CELLPHONE'].isin(['Samsung Galaxy J3 (8GB)'])]
if Lenovo.empty:
    print("Lenovo表格为空")
else:
    print("Lenovo表格不为空")
Lenovo = Lenovo['REVIEW']



pipeline = Pipeline([('feature_extraction', TfidfVectorizer()), ('cluster', KMeans(n_clusters=n_clusters))])
pipeline.fit(Lenovo)
labels = pipeline.predict(Lenovo)
c = Counter(labels)
for cluster_number in range(n_clusters):
    print("Cluster {} contains {} samples".format(cluster_number, c[cluster_number]))
Lenovo = pd.DataFrame(Lenovo)
Lenovo.insert(1, "Cluster", labels, True)
Lenovo.to_csv("/Users/wzhao/Documents/"+phone_name+str(n_clusters)+".csv")

