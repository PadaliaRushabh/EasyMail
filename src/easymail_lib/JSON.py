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
    import os
    if os.path.isfile(this.file) is True:
      try:
        with open(this.file, this.mode) as json_file:
          return json.load(json_file)
      except ValueError:
        return None
    else:
      open(this.file , "w").close()
      return None

  def write_json_to_file(this):
    pprint(this.json_data)
    open(this.file , "w").close() #clear the file to fix extra bracket bug
    with open(this.file, this.mode) as json_file:
        return json.dump(this.json_data , json_file,indent = 4 , sort_keys=True)

  def update_json(this,json_data,default):
      this.json_data.update(json_data)

  def create_and_update_json_when_default_is_false(this,name,password,email,domain,server,default , new = False):
    j_data = {
      name:{
      "password": password,
      "email": email,
      "domain": domain,
      "server": server
      }
    }
    if new is not True:
      this.update_json(j_data,default)
    else:
      this.set_json_data(j_data)

  def create_and_update_json_when_default_is_true(this,name,password,email,domain,server,default , new = False):
    if new is not True:
      defaultKey = this.json_data.get("default", False)
      if defaultKey is False:
        this.default_doesnot_exists(name,password,email,domain,server,default)
      else:
        this.default_exists(name,password,email,domain,server)
    else:
        this.default_doesnot_exists(name,password,email,domain,server,default, new = True)

  def default_doesnot_exists(this,name,password,email,domain,server,default, new = False):
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
    if new is not True:
      this.update_json(j_data,default)
    else:
      this.set_json_data(j_data)

  def default_exists(this,name,password,email,domain,server):
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

  def convert_to_json(this,name,password,email,domain,server,default):
    if this.json_data is not None:
      if default is False:
        this.create_and_update_json_when_default_is_false(name,password,email,domain,server,default)
      else:
        this.create_and_update_json_when_default_is_true(name,password,email,domain,server,default)
    else:
      if default is False:
        this.create_and_update_json_when_default_is_false(name,password,email,domain,server,default, new = True)
      else:
        this.create_and_update_json_when_default_is_true(name,password,email,domain,server,default, new = True)
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
  json.convert_to_json("Persodnal" , "4545", "email@emaidfdl.com" , "smtp.emaildfdf.com" , "smtp.dfdfemail.com" , True)
  json.write_json_to_file()




if __name__ == "__main__":
  main()
