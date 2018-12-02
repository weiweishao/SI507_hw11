from secrets import *
import requests
from flask import Flask, url_for


# return a formated string ready to be put on the html
def get_stories():
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params={'api-key': nyt_key}
    return requests.get(baseurl, params).json()

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        headlines.append(r['title'])
        headlines.append(r['url'])
    return headlines

def get_5_news(headlines):
    results = '<ol>\n'
    for i in range(5):
        results += '<li>{} ({})</li>\n'.format(headlines[2*i],headlines[2*i+1])
    results += '</ol>'
    return results

                
story_list_json = get_stories()
headlines = get_headlines(story_list_json)
top_news = get_5_news(headlines)
    


app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/user/<username>')
def news(username):
    st1 = '<h1>Hello, {}!</h1>'.format(username)
    st2 = "<h2>Today's top headers in technology are...</h2>"
    st3 = top_news
    html = st1 + st2 + st3
    return html



if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)

