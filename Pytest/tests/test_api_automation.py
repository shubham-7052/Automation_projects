import requests
from collections import Counter

def test_post_request():

    String = 'ABCDBDB'

    freq_map = Counter(String)

    print(freq_map)