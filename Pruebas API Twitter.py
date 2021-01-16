# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:45:30 2021

@author: macabrera
"""

### PRUEBA API TWITTER ###

import requests
import json
import pandas as pd
import time
import tweepy

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAathHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


## PRUEBA INFO DE MI CUENTA

mi_info = api.me()



### info de otro usuario ##

nike = api.get_user('nike')



### extraer followers

followers = api.followers(screen_name = 'nike')

len(followers)

x = 10

for user in tweepy.Cursor(api.followers,screen_name = 'nike').items(x):
    print(json.dumps(user._json, indent=2))


### obtener amigos
    
for user in tweepy.Cursor(api.friends,screen_name = 'nike').items(x):
    print(json.dumps(user._json, indent=2))


## obtener timeline

for timeline in tweepy.Cursor(api.user_timeline,screen_name = 'nike', tweet_mode = 'extended'):
    print(json.dumps(timeline._json, indent=2))


## como buscar tweets

for tweet in tweepy.Cursor(api.search, q = 'mundial de clubes', tweet_mode = 'extended').item(10):
    print(json.dumps(tweet._json, indent=2))
    



### twittear de mi cuenta 

api.update_status('hola desde python')

    
### para retwittear

ultimo_tweet_id = ''

api.retweet(ultimo_tweet_id)


## Dar like a un tweets

data = api.me()

id_ultimo_tweet = data._json['status']['id']

#dar like
api.create_favorite(id_ultimo_tweet)

#quitar like
api.destroy_favorite(id_ultimo_tweet)

## reponder a un tweet

api.update_status('hola hola', in_reply_status_id = id_ultimo_tweet)



## seguir una cuenta 

api.create_friendship('nombre_cuenta')


## dejar de seguir una cuenta

api.destroy_friendship('nombre_cuenta')

## bloquear cuenta

api.create_block('nombre_cuenta')

## desbloquear cuentas

api.destroy_block('nombre_cuenta')

## enviar direct

api.send_direct_message('recipient_id', 'text')




##### datos streaming en twitter


class TweetsListener(tweepy.StreamListener):
    
    def on_connect(self):
        print('Estoy Conectado')
        
    def on_status(self, status):
        print(status.text)
        ## guardar en bbdd
        
    def on_error(self, status_code):
        print('Error ',status_code)
    

stream = TweetsListener()

streamingAPI = tweepy.Stream(auth=api.auth, listener = stream)
   
## para usuarios por id usuario     
streamingAPI.filter(
    follow = ['id_usuarios']
    )

### por palabras claves
streamingAPI.filter(
    track = ['coronavirus']
    )

### por region geografica
streamingAPI.filter(
    locations = [boundingBox]
    )