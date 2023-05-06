from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Load the submission.csv file into a Pandas DataFrame
df = pd.read_csv("submission.csv")

# Set the id column as the index for easier lookup
df = df.set_index('IDLink')

@app.route('/', methods=['GET'])
def get_sentiment():
    # Get the id parameter from the request URL
    id = request.args.get('IDLink')

    # Lookup the SentimentTitle and SentimentHeadline values for the given id
    sentiment_title = df.at[str(id), 'SentimentTitle']
    sentiment_headline = df.at[str(id), 'SentimentHeadline']

    # Return a JSON response with the SentimentTitle and SentimentHeadline values
    return {
        "SentimentTitle": sentiment_title,
        "SentimentHeadline": sentiment_headline
    }

if __name__ == '__main__':
    app.run()