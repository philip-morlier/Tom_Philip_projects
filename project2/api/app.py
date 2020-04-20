# Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#DB engine setup
engine = create_engine("sqlite:///../Database_stuff/trends.sqlite")
conn = engine.connect()

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"/api/v1.0/trends2019<br/>"
        f"/api/v1.0/trends2020<br/>"
        f"/api/v1.0/netflixTweet<br/>"
        f"/api/v1.0/nraTweet<br/>"
    )

@app.route("/api/v1.0/trends2019")
def trends2019():
    result = engine.execute("SELECT * FROM trends2019")
    trends2019={}
    date = []
    guns = []
    virus = []
    boredom = []
    ammo = []
    gun_stores = []
    ar15=[]
    disinfectant=[]
    bleach=[]
    tp=[]
    netflix=[]
    porn=[]
    diy=[]
    for row in result:
        date.append(row[1])
        guns.append(row[2])
        virus.append(row[3])
        boredom.append(row[4])
        ammo.append(row[5])
        gun_stores.append(row[6])
        ar15.append(row[7])
        disinfectant.append(row[8])
        bleach.append(row[9])
        tp.append(row[10])
        netflix.append(row[11])
        porn.append(row[12])
        diy.append(row[13])
    result.close()
    trends2019["date"] = date
    trends2019["guns"] = guns   
    trends2019["virus"] = virus   
    trends2019["boredom"] = boredom   
    trends2019["ammo"] = ammo   
    trends2019["gun_stores"] = gun_stores   
    trends2019["ar15"] = ar15   
    trends2019["disinfectant"] = disinfectant   
    trends2019["bleach"] = bleach   
    trends2019["tp"] = tp   
    trends2019["netflix"] = netflix   
    trends2019["porn"] = porn   
    trends2019["diy"] = diy
    return jsonify(trends2019)

@app.route("/api/v1.0/trends2020")
def trends2020():
    result = engine.execute("SELECT * FROM trends2020")
    trends2020={}
    date = []
    guns = []
    virus = []
    boredom = []
    ammo = []
    gun_stores = []
    ar15=[]
    disinfectant=[]
    bleach=[]
    tp=[]
    netflix=[]
    porn=[]
    diy=[]
    for row in result:
        date.append(row[1])
        guns.append(row[2])
        virus.append(row[3])
        boredom.append(row[4])
        ammo.append(row[5])
        gun_stores.append(row[6])
        ar15.append(row[7])
        disinfectant.append(row[8])
        bleach.append(row[9])
        tp.append(row[10])
        netflix.append(row[11])
        porn.append(row[12])
        diy.append(row[13])
    result.close()
    trends2020["date"] = date
    trends2020["guns"] = guns   
    trends2020["virus"] = virus   
    trends2020["boredom"] = boredom   
    trends2020["ammo"] = ammo   
    trends2020["gun_stores"] = gun_stores   
    trends2020["ar15"] = ar15   
    trends2020["disinfectant"] = disinfectant   
    trends2020["bleach"] = bleach   
    trends2020["tp"] = tp   
    trends2020["netflix"] = netflix   
    trends2020["porn"] = porn   
    trends2020["diy"] = diy
    return jsonify(trends2020)

@app.route("/api/v1.0/cdc_tweet")
def cdc_tweet():
    result = engine.execute("select * from cdcTweet")
    cdcTweet= {}
    tweet = []
    for row in result:
        tweet.append(row[2])
    cdcTweet['tweet'] = tweet
    return jsonify(cdcTweet)

@app.route("/api/v1.0/netflixTweet")
def netflixTweet():
    result = engine.execute("select * from netflix_tweet")
    netflixTweet= {}
    tweet = []
    for row in result:
        tweet.append(row[2])
    netflixTweet['tweet'] = tweet
    return jsonify(netflixTweet)

@app.route("/api/v1.0/nraTweet")
def nraTweet():
    result = engine.execute("select * from nraTweet")
    nraTweet= {}
    tweet = []
    for row in result:
        tweet.append(row[2])
    nraTweet['tweet'] = tweet
    return jsonify(nraTweet)