This Python package provides a comprehensive set of functions for cleaning text data. 
It can remove HTML code, hyperlinks, special characters, punctuation, emojis, and basic stopwords from text. 
It can also convert text to lowercase and tokenize it. The package can return the tokenized text, or it can lemmatize or stem the text, depending on the user's preference.


To install the package, run the following command:

pip install jani_text_cleaning


Usage:

from jani_text_cleaning import NLPCleaning()

a = NLPCleaning(input_text="""This is a sentence with some verbs like running, dancing,etc,... and a hyperlink: https://www.google.com.Punctuations like?.,.!!! emoji👋👋😊😊😊 some custom stopwords which we wont need like alpha,beta,gamma,etc...,.,}""",custom_stopwords=['alpha','beta','Gamma'],method='l')


clean = a.clean()
print(clean)
