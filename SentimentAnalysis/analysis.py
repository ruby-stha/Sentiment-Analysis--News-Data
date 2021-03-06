#importing necessary modules
import re

import nltk
import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics

#downloading required stop words from nltk and importing the stopwords from nltk corpus
nltk.download('stopwords')
from nltk.corpus import stopwords

#using flask for front end hence importing the render_template for rendering the html files

#df is the dataframe which is training set panda object
df = pd.DataFrame()
#tf is the dataframe which is testing set panda object
tf = pd.DataFrame()

#creating objects
df = pd.read_csv('/home/rubyshrestha/sentiment/Sentiment-Analysis--News-Data/SentimentAnalysis/news_data.csv')
tf = pd.read_csv('/home/rubyshrestha/sentiment/Sentiment-Analysis--News-Data/SentimentAnalysis/testData.csv')

#preprocessing training set text by removing non-words from training set text
def preprocessor(text):
       text = re.sub('[\W]+', ' ', text)
       return text

df['news']=df['news'].apply(preprocessor)
print(df['news'])

#removing stop words from training set text
stop = stopwords.words('english')
def remove_stop_words(text):
       return [w for w in text.split() if w not in stop]

df['news']=df['news'].apply(remove_stop_words)
print(df['news'])

val=0
porter = PorterStemmer()
for x in df['news']:
    df['news'][val] = [porter.stem(word) for word in x]
    text=""
    for word in df['news'][val]:
        text=text + word + " "
    df['news'][val]=text
    val+=1
print(df['news'])

#testing usage of CountVextorizer and Tfidfransformer which computes tfidf
count = CountVectorizer()
bag = count.fit_transform(df['news'])
print(count.vocabulary_)

print(bag.toarray())

tfidf = TfidfTransformer()
np.set_printoptions(precision=2)
print(tfidf.fit_transform(count.fit_transform(df['news'])).toarray())

#Applying logistic regression classifier with L2 regularization and λ=3)
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', LogisticRegression(C=3))])

_ = text_clf.fit(df['news'],df['sentiment'])

#get predicted values
predicted = text_clf.predict(tf['news'])
print(predicted)

#filling good and bad lists
good=[]
bad=[]
ind=0

accuracyPercent=np.mean(predicted == tf['sentiment'])
print("Accuracy: "+ str(accuracyPercent))

print(":::Confusion Matrix:::")
print(metrics.confusion_matrix(tf['sentiment'],predicted))

for p in predicted:
	if p==0:
		bad.append(tf['news'][ind])
		ind+=1
	else:
		good.append(tf['news'][ind])
		ind+=1
	



def myfunction():
	return bad, good, accuracyPercent






