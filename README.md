# Sentiment-Analysis--News-Data
The prototype was initially developed during 24 hr hackathon, year: 2018 by the following team members.

<b>Team Members: (in alphabetical order) <br/></b>
Asmita Subedi, Mohan Singh Bomrel, Ruby Shrestha and Yashin Shekh

# Background:

Sentiment Analysis is a fun task to do. It is making sense of the emotional tone or characteristic of any piece of subjective information, be it in any form of media. One of the most popular versions of sentiment analysis is classifying the collective series of words into one of the three classes of sentiments: positive, negative or neutral.
 
In broad terms, sentiment analysis requires five distinctive steps:

1. Collection of subjective information (multiple paragraphs, to be specific) for finding pattern in positive and negative sentiments <br/>
2. Preprocessing them using the techniques of natural language processing<br/>
3. Determining features / feature selection<br/>
4. Training the classifier<br/>
5. Testing the classifier on some test paragraph/ series of words<br/>

As a team of four, I, along with three of my friends (Asmita Subedi, Mohan Singh Bomrel and Yashin Shekh), decided to carry out sentiment analysis of the news posted online in one of the popular news daily of Nepal, [The Kathmandu Post](http://kathmandupost.ekantipur.com/). We wanted to build a classifier which could categorize a particular news article as good or bad, meaning having positive sentiment or negative sentiment respectively. All four of us worked together throughout the development process with Mr. Shekh focused on web scraping / data extraction, Miss Subedi focused on front end and data preparation, and I, along with Mr. Bomrel, focused on Research and Text Analysis.

# Data Collection and Preparation:

Majority of the news data to work on were collected via web scraping. The data were either news headlines or around 150 words news content extracted from The Kathmandu Post. In addition to such extracted news data, around 60 training data were self-created examples of positive/negative sentences most likely to encounter in news articles. The example positive and negative sentences were inserted in the data so that our classifier would have an easy time understanding the sentence sentiment (+/-).

After the news data were collected in csv file, each of the news data was provided with sentiments (0 for negative and 1 for positive). With this, a total of 247 data were prepared out of which we used 135 data for training purpose and 112 for testing purpose (that is, around 55% for training and 45% for testing).

I have briefed on Data Preprocessing, Feature Extraction and Training/Classification in my [site](https://ruby-shrestha.000webhostapp.com/news-data-sentiment-analysis/)

<b>Note: </b> I have made some minor improvements over time after the hackathon.
