# REFERENCES:
# https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/
# https://textblob.readthedocs.io/en/dev/quickstart.html


from textblob import TextBlob

blob = TextBlob("I really like ice cream")

# Identify and print noun phrases
print(blob.noun_phrases)

# Print sentiment polarity score
# 0.0 is very objective and 1.0 is very subjective
print(blob.sentiment)

