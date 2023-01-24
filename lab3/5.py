record_collection = {2548: {'albumTitle': 'Slippery When Wet',
                            'artist': 'Bon Jovi',
                            'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
                     2468: {'albumTitle': '1999',
                            'artist': 'Prince',
                            'tracks': ['1999', 'Little Red Corvette']},
                     1245: {'artist': 'Robert Palmer','tracks': []},
                     5439: {'albumTitle': 'ABBA Gold'}}

def update_records(dictionary_record, id, property, value):
       if id in dictionary_record.keys():
              if value == '':
                     del dictionary_record[id][property]
              elif (property == 'tracks' and not ('tracks' in record_collection[id])):
                     dictionary_record[id]['tracks'] = [value]
              elif (property == 'tracks' and dictionary_record[id][property] != None):
                     dictionary_record[id]['tracks'].append(value)
              elif (property != 'tracks'):
                     dictionary_record[id].update({property : value})
       return dictionary_record

print(update_records(record_collection, 5439,'tracks', '2000'))