# from flask import Flask, request
# import pandas as pd

# app = Flask(__name__)

# # Load the submission.csv file into a Pandas DataFrame
# df = pd.read_csv("submission.csv")

# # Set the id column as the index for easier lookup
# df = df.set_index('IDLink')

# @app.route('/', methods=['GET'])
# def get_sentiment():
#     # Get the id parameter from the request URL
#     id = request.args.get('IDLink')

#     # Lookup the SentimentTitle and SentimentHeadline values for the given id
#     sentiment_title = df.at[str(id), 'SentimentTitle']
#     sentiment_headline = df.at[str(id), 'SentimentHeadline']

#     # Return a JSON response with the SentimentTitle and SentimentHeadline values
#     return {
#         "SentimentTitle": sentiment_title,
#         "SentimentHeadline": sentiment_headline
#     }

# if __name__ == '__main__':
#     app.run()


from flask import Flask, request, render_template
import pandas as pd
import json

app = Flask(__name__)

# Load the submission.csv file into a Pandas DataFrame
df = pd.read_csv("submission.csv")

# Set the id column as the index for easier lookup
df = df.set_index('IDLink')

@app.route('/', methods=['GET', 'POST'])
def get_sentiment():
    # if request.method == 'GET':
        # Get the IDLink value from the request form data
    id = request.form['IDLink']

    # Lookup the SentimentTitle and SentimentHeadline values for the given id
    sentiment_title = df.at[str(id), 'SentimentTitle']
    sentiment_headline = df.at[str(id), 'SentimentHeadline']

    result = {
        "sentiment_title":sentiment_title,
        "sentiment_headline" : sentiment_headline
    }

    # Return the HTML template with the SentimentTitle and SentimentHeadline values
    # return render_template('index.html', sentiment_title=sentiment_title, sentiment_headline=sentiment_headline)
    return json.dump(result)

    # Return the HTML template for the initial GET request
    # return render_template('index.html')

if __name__ == '__main__':
    app.run()