import pickle
from configparser import ConfigParser
import httpx
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

config = ConfigParser()
config.read('credentials.ini')
api_key = config['BingAPI']['api_key']

web_search_endpoint = "https://api.bing.microsoft.com/v7.0/search"

headers = {
    'Ocp-Apim-Subscription-Key': api_key
}

query = 'the Qutb Shahi dynastys Muhammad Quli Qutb Shah established Hyderabad in 1591 to extend the capital beyond the fortified Golconda.'
tokens = word_tokenize(query)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
stemmed_text = ' '.join(stemmed_tokens)
query = stemmed_text

results = []

for i in range(0, 201, 50):
    params = {
        'q': query,
        'count': 50,
        'offset': i,
        'mkt': 'en-US',
        'freshness': 'Month',
        'answerCount': 2
    }
    response = httpx.get(web_search_endpoint, headers=headers, params=params)
    result = response.json()
    results.extend(result['webPages']['value'])
df = pd.DataFrame(results)

# Save DataFrame as a pickle file
with open('search_results.pkl', 'wb') as f:
    pickle.dump(df, f)