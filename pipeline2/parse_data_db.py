#parse the data from the api to get the value of generated keypoints
import wget
import json
from natsort import natsorted, ns
import random


#url = 'http://127.0.0.1:8080/poses'
#filename = wget.download(url,out='./Api_json')

with open('./poses') as file:
    document = json.load(file)
#    print(document)
print(len(document))
#print(natsorted(list(document[0].items()))[2][1])
#print(natsorted(list(natsorted(list(document[0]['pose'].items()))[0])[0]))
#print(natsorted(list(natsorted(list(document[0]['pose'].items()))[0])[1]))
for i in range(len(document)):

    data ={
        "version":1.3,
        "people":natsorted(list(natsorted(list(document[i]['pose'].items()))[0])[1]),
        "file":str(document[i]['file']),
        "id":str(random.randint(1,21)*5)

    }

    with open('./api_json/' + document[i]['file'] + '.json', 'w') as outfile:
        json.dump(data, outfile)
