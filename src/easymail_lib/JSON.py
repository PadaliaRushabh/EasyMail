#!/usr/bin/env python3


import json
from pprint import pprint

class JSON(object):

  #json_data = []
  def __init__(this,file,mode = 'r+'):
    this.file = file
    this.mode = mode

  def set_file(this, file , mode):
    this.file = file
    this.mode = mode

  def set_json_data(this, json_data):
    #this.json_data = []
    this.json_data = json_data
    #this.json_data.append(json_data)


  def reinitialize_json_data(this, json_data):
    this.json_data = []
    this.json_data.append(json_data)

  def append_json_data(this, json_data):
    this.json_data.append(j_data)

  def read_json_from_file(this):
    with open(this.file, this.mode) as json_file:
      #this.json_data = json.load(json_file)
      #pprint(this.json_data)
      #return json.dump(this.json_data , indent = 4 , sort_keys=True)
      return json.load(json_file)

  def write_json_to_file(this):
    with open(this.file, this.mode) as json_file:
        return json.dump(this.json_data , json_file,indent = 4 , sort_keys=True)

  def convert_to_json(this,name,password,email,domain,server,default):
'''
    if default is True:
      j_data = {
        name:{
        "password": password,
        "email": email,
        "domain": domain,
        "server": server
        }
      }
      this.json_data.append(j_data)
      pprint(this.json_data)
      #check if any email is default
      defaultkey = False;
      complete_json = []
      for json in this.json_data:
        print('next')
        pprint(json)
        defaultKey = json.get("default", False)

        if defaultKey is not False: #if False then make a new entry
          json['default']['account_name'] = name #else update the default value to the new value

          #this.reinitialize_json_data(json)


      if defaultKey is False:
        j_data= {
          "default":{
          "account_name":name
          }
        }
        this.json_data.append(j_data)

    else:
      j_data = {
        name:{
        "password": password,
        "email": email,
        "domain": domain,
        "server": server
        }
      }
      this.json_data.append(j_data)

'''

def main():

  from pprint import pprint
  FILE = "/home/rushabh/Rushabh/EasyMail/src/config/EasyMail.json"
  json = JSON(FILE)
  '''
  json_data = json.read_json_from_file()
  d = None
  for j in json_data:
    d = j.get("default", None)
    if d is not None:
        j['default']['account_name'] = "neweraccount"
        print(j)
  json.set_json_data(j)
  json.write_json_to_file()
  '''
  json_data = json.read_json_from_file()
  json.set_json_data(json_data)
  json.convert_to_json("dsddf" , "newpass", "email@email.com" , "smtp.email.com" , "smtp.email.com" , True)
  #json.write_json_to_file()
  #pprint(json_data[1])



if __name__ == "__main__":
  main()
