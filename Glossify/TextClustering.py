import pickle
import os
import sys
import re
from xml_to_text import xml_to_dict, join_as_str, xml_to_str
from lex_to_dict import to_dict
import pdb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def find_optimal_clusters(data, max_k):
    iters = range(2, max_k + 1, 2)

    sse = []
    for k in iters:
        sse.append(MiniBatchKMeans(n_clusters=k, init_size= 200, batch_size=50, random_state=20).fit(data).inertia_)
        print('Fit {} clusters'.format(k))

    f, ax = plt.subplots(1, 1)
    ax.plot(iters, sse, marker='o')
    ax.set_xlabel('Cluster Centers')
    ax.set_xticks(iters)
    ax.set_xticklabels(iters)
    ax.set_ylabel('SSE')
    ax.set_title('SSE by Cluster Center Plot')
    print(sse)
    return min(sse)


def plot_tsne_pca(data, labels):
    print("labels")
    print(labels)
    max_label = max(labels)
    pca = PCA(n_components=2).fit_transform(data.todense())
    tsne = TSNE().fit_transform(PCA(n_components=50).fit_transform(data.todense()))
    LABEL_COLOR_MAP = {0: '0.0', 1: '0.05', 2: '0.1', 3: '0.15', 4: '0.2', 5: '0.25', 6: '0.3', 7: '0.35', 8: '0.4', 9: '0.45', 10: '0.5', 11: '0.55', 12: '0.6', 13: '0.65', 14: '0.7', 15: '0.75', 16: '0.8', 17: '0.85', 18: '0.9', 19: '0.95'}
    label_color = [LABEL_COLOR_MAP[l] for l in labels]
    f, ax = plt.subplots(1, 2, figsize=(14, 6))

    ax[0].scatter(pca[:, 0], pca[:, 1], c= label_color)
    ax[0].set_title('PCA Cluster Plot')

    ax[1].scatter(tsne[:, 0], tsne[:, 1], c= label_color)
    ax[1].set_title('TSNE Cluster Plot')
    plt.show()
    plt.savefig("clusterReport.png")

def main():
    file_list = [f for f in os.listdir('./ecgen-radiology') if os.path.isfile(os.path.join('./ecgen-radiology', f))]
    listText =[]
    for filename in file_list:
        text = xml_to_str("ecgen-radiology/" + filename)
        text = text.replace("\n", " ")
        listText.append(text)
    listText = np.array(listText)
    print(listText)
    tfidf = TfidfVectorizer(
        min_df=5,
        max_df=0.95,
        max_features=8000,
        stop_words='english'
    )
    tfidf.fit(listText)
    Text = tfidf.transform(listText)
    lowestsse = find_optimal_clusters(Text, 20)
    clusters = MiniBatchKMeans(n_clusters= 8, init_size=200, batch_size= 50, random_state=20).fit_predict(Text)
    np.set_printoptions(threshold=sys.maxsize)
    plot_tsne_pca(Text, clusters)


# boilerplate for terminal compatability
if __name__ == '__main__':
    main()
