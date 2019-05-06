#!/usr/bin/env python
import pika,sys
sys.path.insert(0,'../')
from model.demographic.recommender import return_top
from model.content_based.recommender import get_recommendations
from model.collaborative.recommender import get_table, get_recommendations_collab
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='query',durable= False)
channel.queue_declare(queue='resultsDemographic',durable=False)
channel.queue_declare(queue='resultsContent',durable= False)
channel.queue_declare(queue='resultsCollab',durable= False)
def callback(ch, method, properties, body):
    requestParams = json.loads(body.decode('utf-8'))
    
    if(requestParams[0]=='content'):
        movie_to_match= requestParams[1]
        print('in content Based menu')
        results = get_recommendations(movie_to_match).to_json(orient='records')
        channel.basic_publish(exchange='',routing_key='resultsContent',body=results)
    elif(requestParams[0]=='collab'):
        print('inside collab')
        userRatings = get_table(requestParams[1]).to_json(orient='records')
        recommendation = get_recommendations_collab(requestParams[1],requestParams[2])
        results = '{"user":'+userRatings+',"result":"'+recommendation+'"}'
        channel.basic_publish(exchange='',routing_key='resultsCollab',body=results)
        
    else:
        
        number_of_movies = int(requestParams[0])
        print('in demographic')
        results = return_top(number_of_movies).to_json(orient='records')
        channel.basic_publish(exchange='',routing_key='resultsDemographic',body=results)

    print(json.dumps(results, ensure_ascii=False))

    # send a message back
    

    # connection.close()

#  receive message and complete simulation
channel.basic_consume(callback,queue='query',no_ack=True)

channel.start_consuming()