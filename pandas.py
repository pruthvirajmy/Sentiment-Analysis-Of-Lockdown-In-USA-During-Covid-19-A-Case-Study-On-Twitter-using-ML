X_train = ["This was really awesome an awesome movie", "Great movie! Ilikes it a lot",
"Happy Ending! Awesome Acting by hero", "loved it!",
"Bad not upto the mark", "Could have been better",
"really Dissapointed by the movie"]


y_train = ["positive","positive","positive","positive","negative","negative","negative"]
X_train
['This was awesome an awesome movie', 'Great movie! Ilikes it a lot',
'Happy Ending! Awesome Acting by hero', 'loved it!',
'Bad not upto the mark', 'Could have been better', 'Dissapointed by the movie']
Cleaning of the data
from nltk.tokenize import RegexpTokenizer from nltk.stem.porter import PorterStemmer from nltk.corpus import stopwords
import nltk nltk.download('stopwords')
[nltk_data] Downloading package stopwords to /root/nltk_data... 
[nltk_data] Package stopwords is already up-to-date!
True
tokenizer = RegexpTokenizer(r"\w+") en_stopwords = set(stopwords.words('english')) ps = PorterStemmer()
def getCleanedText(text):
text = text.lower()
tokens = tokenizer.tokenize(text)
new_tokens = [token for token in tokens if token not in en_stopwords] stemmed_tokens = [ps.stem(tokens) for tokens in new_tokens] clean_text = " ".join(stemmed_tokens)
return clean_text X_test = ["it was bad"]
X_clean = [getCleanedText(i) for i in X_train] xt_clean = [getCleanedText(i) for i in X_test]
X_clean
['awesom awesom movi', 'great movi ilik lot',
'happi end awesom act hero', 'love',
'bad upto mark', 'could better', 'dissapoint movi']
X_train = ["This was awesome an awesome movie", "Great movie! Ilikes it a lot",
"Happy Ending! Awesome Acting by hero", "loved it!",
"Bad not upto the mark", "Could have been better", "Dissapointed by the movie"]
[ ]
X_train = ["This was really awesome an awesome movie", "Great movie! Ilikes it a lot",
"Happy Ending! Awesome Acting by hero", "loved it!",
"Bad not upto the mark", "Could have been better",
"really Dissapointed by the movie"]


y_train = ["positive","positive","positive","positive","negative","negative","negative"]

[ ]
X_train
['This was awesome an awesome movie', 'Great movie! Ilikes it a lot',
'Happy Ending! Awesome Acting by hero', 'loved it!',
'Bad not upto the mark', 'Could have been better', 'Dissapointed by the movie']
Cleaning of the data [ ]

# "I am a python dev" -> ["I", "am", "a", "python", "dev"] [ ]
from nltk.tokenize import RegexpTokenizer # NLTK -> Tokenize -> RegexpTokenizer
[ ]
# Stemming
# "Playing" -> "Play"
# "Working" -> "Work" [ ]
from nltk.stem.porter import PorterStemmer # NLTK -> Stem -> Porter -> PorterStemmer

from nltk.corpus import stopwords # NLTK -> Corpus -> stopwords
[ ]
# Downloading the stopwords import nltk nltk.download('stopwords')
[nltk_data] Downloading package stopwords to /root/nltk_data... [nltk_data] Package stopwords is already up-to-date!
True [ ]
tokenizer = RegexpTokenizer(r"\w+") en_stopwords = set(stopwords.words('english')) ps = PorterStemmer()
[ ]
def getCleanedText(text):
text = text.lower()


# tokenizing
tokens = tokenizer.tokenize(text)
new_tokens = [token for token in tokens if token not in en_stopwords] stemmed_tokens = [ps.stem(tokens) for tokens in new_tokens] clean_text = " ".join(stemmed_tokens)
. return clean_text Input from the user [ ]
X_test = ["it was bad"] [ ]

[ ]
X_clean = [getCleanedText(i) for i in X_train] xt_clean = [getCleanedText(i) for i in X_test] [ ]
X_clean
['awesom awesom movi', 'great movi ilik lot',
'happi end awesom act hero', 'love',
'bad upto mark', 'could better'
'dissapoint movi'] [ ]
# Data before cleaning '''
X_train = ["This was awesome an awesome movie", "Great movie! Ilikes it a lot",
"Happy Ending! Awesome Acting by hero", "loved it!",
"Bad not upto the mark", "Could have been better", "Dissapointed by the movie"]
'''

Vectorize [ ]
↳ 7 cells hidden Multinomial Naive Bayes [ ]
↳ 11 cells hidden
Colab paid products - Cancel contracts here
