#  Music Playlist Recommendation Engine

---

## Goals:

The goal of this analysis is to leverage publicly available Spotify song data to build a recommendation engine that could be used to extend a user playlist or a Spotify curated playlist. While Spoitfy makes an array of track/artist meta data available via their API, this recommendation engine will focus on leveraging artist meta data, associated artist genres, track meta data, and the audio features of a song.

While the immediate business use-case is specific music recommendations, the broader application of this analysis could be applied to any item-based recommendation engine (i.e. product recommendations on an e-commerce site).

---


## Technical Report:
An in depth discussion of this project is found in the [technical report](https://github.com/davidcbickham/Capstone).

---


## Technologies Used:

Data Collection: [Spotipy API](https://spotipy.readthedocs.io/en/latest/)

Data Management: [numpy](https://docs.scipy.org/doc/numpy/reference/), [pandas](https://pandas.pydata.org/pandas-docs/stable/)

Feature Engineering: [scikit-learn](https://scikit-learn.org/stable/documentation.html) - [Singular Value Decomposition](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html), [HDBSCAN](https://hdbscan.readthedocs.io/en/latest/index.html)


---

 