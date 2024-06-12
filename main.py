from textblob import TextBlob
from newspaper import Article

T = "A recent study published in a leading medical journal presents mixed findings on the effectiveness of a newly developed flu vaccine. The study, conducted over a period of two years with a large sample size, suggests that while the vaccine showed promising results in certain demographics, its overall effectiveness varied widely. Researchers caution that further investigation is needed to determine the vaccine's long-term efficacy and its potential impact on public health strategies for combating influenza."
article = Article(T)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to +1
print(sentiment)





