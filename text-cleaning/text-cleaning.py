from bs4 import BeautifulSoup
from html import parser

tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# HTMLParser is a class
# parser = HTMLParser()
soup = BeautifulSoup(tweet, 'html.parser')
print(soup)
decoded_tweet = tweet.encode('ascii', 'ignore')
print(decoded_tweet)
# create
APPOSTOPHES = {
    "'s": " is",
    "'re": " are"
}

words = tweet.split()
reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
reformed = " ".join(reformed)
print(reformed)

