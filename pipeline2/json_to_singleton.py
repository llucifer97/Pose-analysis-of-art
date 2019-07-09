import json
import random
import os
path_to_json = './api_json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
json_arr2 = list()
for json_file in json_files:
    json_file_path = os.path.join(path_to_json, json_file)
    with open(json_file_path, "r") as f:
        json_arr2.append(json.load(f))



print('sorting the json files in natural way!')
from natsort import natsorted, ns
# This is the path where all the files are stored.
json_path2 = './api_json'
# Open one of the files,
lst2 = []
for data_file2 in os.listdir(json_path2):
    lst2.append(data_file2)
    print(data_file2)
json_file2 = lst2
print(".......")
print(json_file2)
len(json_file2)


peeps2 = []
for j in range(0,len(json_arr2)):
    peeps2.append(len(natsorted(json_arr2)[j]['people']))
print('collection the number poses of from different json files completed!')

print('mapping the json file and no of pose!')
#lets connect the number of peeps,json file name and arr[] i.e keypoints
mapped2 = zip(json_file2, peeps2)
# converting values to print as set
mapped2 = set(mapped2)
json_to_peeps2 = list(mapped2)
json_to_peeps2 = natsorted(json_to_peeps2)
#json_to_peeps2

for j in range(len(json_to_peeps2)):

    for i in range(json_to_peeps2[j][1]):

        with open('./api_json/' + json_to_peeps2[j][0]) as file:
            single_pose = json.load(file)
            print(single_pose['people'][i])
        #print(len(document))

        data ={
            "version":1.3,
            "people":single_pose['people'][i],
            "file":str(single_pose['file']),
            "id":str(random.randint(1,101)*7)

        }

        with open('./json_single_pose/' + single_pose['file'] +str(i) + '.json', 'w') as outfile:
            json.dump(data, outfile)


