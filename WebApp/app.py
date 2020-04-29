from flask import Flask, render_template,request, make_response
import os
import praw
import urllib.request, json
from utils import getPostDetails,getFlair,clean
app = Flask(__name__)
 


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/automated_testing")
def automated_testing():
    return render_template("automated_testing.html")

# LINK (greater efficiency)
def predictFlairByLink(postLink):
    predictedFlair = {'flair':postLink}
    #remaining code goes here
    predictedFlair['flair'] = getPostDetails(postLink)
    return predictedFlair


# TITLE (efficiency will be lesser)
def predictFlairByTitle(postTitle):
    predictedFlair = {'flair':getFlair({'text':clean(postTitle)})}
    #remaining code goes here
    print(predictedFlair['flair'])
    return predictedFlair


@app.route('/getLink', methods=['GET'])
def getLink():
    postLink=request.args.get('link')
    print(postLink)
    predictedFlair = predictFlairByLink(postLink)
    return predictedFlair

@app.route('/getTitle', methods=['GET'])
def getTitle():
    postTitle=request.args.get('title')
    print(postTitle)
    predictedFlair = predictFlairByTitle(postTitle)
    return predictedFlair


if __name__ == "__main__":
    app.run(debug=True,port=int(os.environ.get('PORT', 8080)))