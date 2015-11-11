#!/usr/bin/env python3
import json
from pprint import pprint

class JSON(object):

  def __init__(self,file,mode = 'r+'):
    self.file = file
    self.mode = mode

  def set_file(self, file , mode):
    self.file = file
    self.mode = mode

  def set_json_data(self, json_data):
      self.json_data = json_data

  def append_json_data(self, json_data):
    self.json_data.append(json_data)

  def read_json_from_file(self):
    import os
    if os.path.isfile(self.file) is True:
      try:
        with open(self.file, self.mode) as json_file:
          return json.load(json_file)
      except ValueError:
        return None
    else:
      open(self.file , "w").close()
      return None

  def write_json_to_file(self):
    pprint(self.json_data)
    open(self.file , "w").close() #clear the file to fix extra bracket bug
    with open(self.file, self.mode) as json_file:
        return json.dump(self.json_data , json_file,indent = 4 , sort_keys=True)

  def update_json(self,json_data,default):
      self.json_data.update(json_data)

  def create_and_update_json_when_default_is_false(self,name,password,email,domain,server,default , new = False):
    j_data = {
      name:{
      "password": password,
      "email": email,
      "domain": domain,
      "server": server
      }
    }
    if new is not True:
      self.update_json(j_data,default)
    else:
      self.set_json_data(j_data)

  def create_and_update_json_when_default_is_true(self,name,password,email,domain,server,default , new = False):
    if new is not True:
      defaultKey = self.json_data.get("default", False)
      if defaultKey is False:
        self.default_doesnot_exists(name,password,email,domain,server,default)
      else:
        self.default_exists(name,password,email,domain,server)
    else:
        self.default_doesnot_exists(name,password,email,domain,server,default, new = True)

  def default_doesnot_exists(self,name,password,email,domain,server,default, new = False):
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
      self.update_json(j_data,default)
    else:
      self.set_json_data(j_data)

  def default_exists(self,name,password,email,domain,server):
    j_data = {
      name:{
      "password": password,
      "email": email,
      "domain": domain,
      "server": server
      }
    }
    self.update_json(j_data,False)

    self.json_data['default']['account_name'] = name

  def convert_to_json(self,name,password,email,domain,server,default):
    if self.json_data is not None:
      if default is False:
        self.create_and_update_json_when_default_is_false(name,password,email,domain,server,default)
      else:
        self.create_and_update_json_when_default_is_true(name,password,email,domain,server,default)
    else:
      if default is False:
        self.create_and_update_json_when_default_is_false(name,password,email,domain,server,default, new = True)
      else:
        self.create_and_update_json_when_default_is_true(name,password,email,domain,server,default, new = True)
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
