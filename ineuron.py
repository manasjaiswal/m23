from flask import Flask,request,jsonify,render_template
from bs4 import BeautifulSoup as bsp
from urllib.request import urlopen as Uq
import requests
app=Flask(__name__)

@app.route('/',methods=['GET'])
def routetolocal():
    return render_template('index1.html')

@app.route('/courseinfo',methods=['GET','POST'])
def detailextracter():

    if request.method=='POST':
        try:
            choicestring=request.form['content'].replace(' ','')
            url='https://ineuron.ai/course/'+choicestring
            client=Uq(url)
            page=client.read()
            client.close()
            tag_page=bs(page,'html.parser')
            basicsection=tag_page.find('section')
        except:
