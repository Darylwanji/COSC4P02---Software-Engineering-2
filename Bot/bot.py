import pickle
# For natural language processing
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
#randomizer
import  random
import os
# To enable json file parsing
import json
import numpy as np
import tensorflow 
from tensorflow.python.framework import ops
import tflearn

# Open the file
with open("sample2.json") as sample:
	data = json.load(sample)
try: 
	with open("data1.pickle", "rb") as f: 
		words, labels, training_ds, op_ds = pickle.load(f)
except:
	words = []
	labels = []
	docs_1 = [] 
	docs_2 = []
	for intent in data["intents"]:
			#stemming each word from list of patterns to get the root word of each of the words 
		for pattern in intent["patterns"]:
			wrds = nltk.word_tokenize(pattern)
			words.extend(wrds)
			docs_1.append(wrds)
			docs_2.append(intent["tag"])
		# getting all keys
		if intent["tag"] not in labels:
			labels.append(intent["tag"])
	# Again stem the list of words 
	words = [stemmer.stem(w.lower()) for w in words if w != "?"]

	# Remove duplicates and get back a list
	words = sorted(list(set(words))) 
	labels = sorted(labels)

	training_ds = []
	op_ds = []

	op_em =[ 0 for _ in range(len(labels))]

	for x, doc in enumerate(docs_1):
		bag = []
		wrds = [stemmer.stem(w) for w in doc]
		for w in words: 
			if w in words:
				bag.append(1)
			else: 
				bag.append(0)
		op_r = op_em[:]
		op_r[labels.index(docs_2[x])] = 1

		training_ds.append(bag)
		op_ds.append(op_r)

	training_ds = np.array(training_ds)
	op_ds = np.array(op_ds)

	with open("data1.pickle","wb") as f: 
		pickle.dump((words,labels,training_ds,op_ds),f)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training_ds[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)

net = tflearn.fully_connected(net, len(op_ds[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training_ds,op_ds,n_epoch=500, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def chat():
    print("Welcome to basic bot")
    while True:
        inp = input("					You: ")
        if inp.lower() == "quit":
            break
        results = model.predict([bag_of_words(inp, words)])
        results_index = np.argmax(results)
        tag = labels[results_index]
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        print("Bot: " + random.choice(responses))
chat()