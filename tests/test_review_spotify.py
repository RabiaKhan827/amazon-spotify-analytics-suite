import unittest
from review_spotify_analytics import AmazonReviewAnalyzer, SpotifyAudioClusterer

class TestReviewSpotify(unittest.TestCase):
    def test_benchmarks(self):
        rev = AmazonReviewAnalyzer().run_benchmark()
        self.assertEqual(rev.sentiment_accuracy, 1.0)
        spot = SpotifyAudioClusterer().run_benchmark()
        self.assertGreater(spot.silhouette_score, 0.80)

if __name__ == "__main__":
    unittest.main()
