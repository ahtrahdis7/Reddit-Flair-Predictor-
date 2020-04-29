import joblib
model = joblib.load('MODEL_1_DEMO.pkl')

# write functions here
def getFlair(data_dict):
    
    pred = model.predict(data_dict)
    return str(pred)

def getPostDetails(URL):
    import praw
    import urllib.request, json
    reddit = praw.Reddit(client_id='RfXfQdzvbbjjqA',
                     client_secret='Maos8fj7b2iDTgaa52opam-7uH4',
                     user_agent='Test',
                    username = 'iamcool_7',
                    password = 'iamcool@77890')
    # fetch data from the URL

    # with urllib.request.urlopen(URL) as url:
    #     data = json.loads(url.read().decode())
    #     print(data.keys)
    data = reddit.submission(url = URL)
    # print("!"+str(data.title))
    if(data.link_flair_background_color == ''):
        data.link_flair_background_color = 'Others'
    print("POST DETAILS REACHED")
    data_dict = {'text': clean(str(data.title)+str(data.selftext))}
    data_dict['text'] = data_dict['text'] + " "+str(data.link_flair_background_color)+" " +str(data.link_flair_text_color)
    print(data_dict)
    print("POST DETAILS EXECUTED")
    flair = getFlair(data_dict)
    print(flair)
    return flair


def clean(text):
    import re
    from nltk.corpus import stopwords 
    PLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))
    text = text.lower() # lowercase text
    text = PLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    return text

