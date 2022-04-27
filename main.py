from fastapi import FastAPI, status

from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")

sentiment_query_sentence = get_random_comment(top_comments)
sentiment = sentiment_model(sentiment_query_sentence)
print(f"Sentiment test: {sentiment_query_sentence} == {sentiment})


app= FastAPI()

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perofrm_healthcheck():
        return {'healthcheck': 'Everthing OK!'}

@app.post("my-endpoint")
def my_endpoint(request: PredictionRequest):
  # YOUR CODE GOES HERE