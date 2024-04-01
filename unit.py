import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):
    def test_website_loading(self):
        print("Testing if atg.world website loads...")

        website_url = "https://atg.world"
        response = requests.get(website_url)
        
        self.assertEqual(response.status_code, 200, f"Failed to load website: {website_url}")
        print("Website loading test completed.")

if __name__ == '__main__':
    unittest.main()
