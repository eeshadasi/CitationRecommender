from flask import Flask, render_template, request
import pickle
import pandas as pd
import httpx
from configparser import ConfigParser
from textblob import TextBlob  # Import TextBlob for sentiment analysis
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    query = request.form['inputText']

    # Processing query
    tokens = word_tokenize(query)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    stemmed_text = ' '.join(stemmed_tokens)
    query = stemmed_text

    # Fetching search results
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['BingAPI']['api_key']
    web_search_endpoint = "https://api.bing.microsoft.com/v7.0/search"
    headers = {'Ocp-Apim-Subscription-Key': api_key}
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
    df = df[['url', 'name', 'snippet']].head(10)

    # Perform sentiment analysis on combined text of input and snippet
    sentiments = []
    for index, row in df.iterrows():
        combined_text = f"{query} {row['snippet']}"
        sentiment_score = TextBlob(combined_text).sentiment.polarity
        sentiments.append(sentiment_score)

    df['sentiment'] = sentiments
    df = df.sort_values(by='sentiment', ascending=False)
    with open('search_results.pkl', 'wb') as f:
        pickle.dump(df, f)

    return render_template('index.html', table=df)

if __name__ == '__main__':
    app.run(debug=True)
