#!/usr/bin/env python3


import json
from pprint import pprint

class JSON(object):

  def __init__(this,file,mode = 'r+'):
    this.file = file
    this.mode = mode

  def set_file(this, file , mode):
    this.file = file
    this.mode = mode

  def set_json_data(this, json_data):
    this.json_data = json_data

  def append_json_data(this, json_data):
    this.json_data.append(j_data)

  def read_json_from_file(this):
    with open(this.file, this.mode) as json_file:
      return json.load(json_file)

  def write_json_to_file(this):
    with open(this.file, this.mode) as json_file:
        return json.dump(this.json_data , json_file,indent = 4 , sort_keys=True)

  def update_json(this,json_data,default):

      this.json_data.update(json_data)

  def _create_and_update_json_when_default_is_false(this,name,password,email,domain,server):
    j_data = {
      name:{
      "password": password,
      "email": email,
      "domain": domain,
      "server": server
      }
    }
    this.update_json(j_data,default)
  def convert_to_json(this,name,password,email,domain,server,default):
    if default is False:
      j_data = {
        name:{
        "password": password,
        "email": email,
        "domain": domain,
        "server": server
        }
      }
      this.update_json(j_data,default)
    else:
      defaultKey = this.json_data.get("default", False)

      if defaultKey is False:
        j_data = {
          name:{
          "password": password,
          "email": email,
          "domain": domain,
          "server": server
          },
          "default": {
          "account_name": name
          }
        }
        this.update_json(j_data,default)
      else:
        j_data = {
          name:{
          "password": password,
          "email": email,
          "domain": domain,
          "server": server
          }
        }
        this.update_json(j_data,False)

        this.json_data['default']['account_name'] = name

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
  json.convert_to_json("falsetry" , "4545", "email@emaidfdl.com" , "smtp.emaildfdf.com" , "smtp.dfdfemail.com" , True)
  json.write_json_to_file()




if __name__ == "__main__":
  main()
