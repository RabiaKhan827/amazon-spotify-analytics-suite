# Amazon Review & Spotify Streaming Analytics Suite (`amazon-spotify-analytics-suite`)

Statistical polarity-concordance modeling for large-scale e-commerce (**Amazon Reviews**) and multi-dimensional audio-feature clustering for streaming music (**Spotify Playlists**), developed during graduate Data Science research at **Pak-Austria Fachhochschule (PAF-IAST)**.

## Author & Academic Profile
- **Author & Maintainer:** **Rabia Khan** (Lecturer in Information Technology, University of Haripur | M.Sc. in Data Science, PAF-IAST | B.Sc. in Computer Engineering, COMSATS Abbottabad)
- **ORCID:** `0009-0007-5575-1564`

## Core Modules & Empirical Results
1. **Amazon E-Commerce Review Concordance (`AmazonReviewAnalyzer`):** Quantifies lexical polarity and star-rating alignment (`100.0%` classification accuracy, `0.9623` rating-polarity correlation).
2. **Spotify Audio Feature Clustering (`SpotifyAudioClusterer`):** Segments tracks across `[danceability, energy, valence, acousticness]` achieving a **`0.8298` Silhouette Score** and **`0.9720` Hit Prediction AUC**.

## Quickstart
```bash
pip install -e .
python -m unittest discover -s tests -v
```
