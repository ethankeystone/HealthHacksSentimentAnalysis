from django.shortcuts import render

from keras import layers, models
import tensorflow as tf
import json
from tensorflow.python.keras.preprocessing.text import tokenizer_from_json

from rest_framework.decorators import api_view
from keras.preprocessing import text, sequence
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def analyzeTweet(request):
	current_folder = 'ML/saved_model/Depression_vs_Suicide/'
	with open(current_folder + 'tokenizer.json') as f:
	    data = json.load(f)
	    tokenizer = tokenizer_from_json(data)

	body_unicode = request.body.decode('utf-8')
	body_data = json.loads(body_unicode)
	data = body_data["input"]
	print(data)
	# data=request.POST
	# answer = {
	# 	"response": data
	# }
	# return Response(answer)
	new_model = tf.keras.models.load_model(current_folder)
	x = sequence.pad_sequences(tokenizer.texts_to_sequences([data]), maxlen=100)

	answer = {
		"response": new_model.predict(x)
	}
	try:	
		return Response(answer)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)
