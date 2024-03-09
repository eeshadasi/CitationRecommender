# Citation Recommender

## Problem Statement
Finding credible sources for citations can be a time-consuming task for editors, researchers, and content creators. This process often involves manually searching for relevant sources that support the content's claims, which can be tedious and inefficient.

##  Overview
This tool aims to improve the quality and credibility of content by providing accurate and relevant source suggestions, ultimately saving time and effort in the research process.

## Features
- Automatically analyzes articles and user queries
- Suggests relevant and credible sources
- Improves the quality and credibility of content
- Saves time and effort in the research process

## Main Functionality
The Credible Source Finder tool uses Flask, pandas, and TextBlob to suggest credible sources for content, aiming to save time and improve content quality. It does this by analyzing user queries and articles, fetching search results using the Bing API, and performing sentiment analysis to rank sources based on relevance and credibility.

**Key Steps:**
- **User Input:** Takes user input from a form.
- **Data Processing:** Processes input by tokenizing, removing stopwords, and stemming words.
- **API Integration:** Uses the Bing API to fetch search results based on the processed query.
- **Sentiment Analysis:** Analyzes the sentiment of the input query and search result snippets.
- **Result Presentation:** Ranks search results based on sentiment and displays them to the user.




## Installation and Running
1. Clone the repository -
    ```bash
    git clone https://github.com/eeshadasi/CitationRecommender.git
    ```
2. Install the required Python packages -

    ```bash
    pip install -r requirements.txt
    ```
3. Set up the configuration file `credentials.ini` with your Bing API key - 
    ```bash
    [BingAPI]
    api_key = YOUR_BING_API_KEY
    ```
4. Run the Flask application -
    ```bash
    python app.py
    ```
5. Access the application in your web browser

## Usage
- Enter a query or article text in the input field.
- Click the "Submit" button to fetch search results and source suggestions.
- The application will display a list of suggested sources based on the analysis.

## Screenshots
![Inital page](https://drive.google.com/uc?export=view&id=1zzhM_f9EbkbS37IW4fIRZrLjxv-NmSdM)

![Try Searching citation](https://drive.google.com/uc?export=view&id=1y5HQbuMx80gG-pdTFFG7Z1wksPdcwF8l)

![Getting Recommendations](https://drive.google.com/uc?export=view&id=1MzUr4zir9C5W7sbj2oebe6nXrRnAnHU_)

## Future Enhancements
- Integration with Citation Hunt to suggest citations and other writing platforms
- Expansion to include additional languages and sources
- Incorporation of user feedback to improve source suggestions over time

## Contributors
- [Eesha Dasi](https://github.com/eeshadasi)
- [Chanda Srija](https://github.com/SrijaC2)
- [Y Vineetha Reddy](https://github.com/vineethayasa)
