import json

dict_data = {
  'user':{
    'name': 'kosei nishi',
    'age': 30 ,
  },
  'country':{
    'name': 'japan',
    'city': ['tokyo','osaka','nagoya'] 
  }
}

json_data = json.dumps(dict_data)
print(json_data)

file = open('test.json','w')
json.dump(json_data,file)
file.close()
