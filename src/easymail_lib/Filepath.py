#!/usr/bin/env python3
import os

class FilePath(object):
  def getSelectedFilepath(this):
    paths = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].splitlines()

    #make files array
    files = []
    #iter over selected file paths
    for f in paths:
      #add to an inner array
      inner=[]
      inner.append(f)
      #add it to the outer file array
      files.append(inner)

    return files

def main():
  filepath = FilePath()
  paths = filepath.getFilename()
  for p in paths:
    print(p)


if __name__ == "__main__":
  main()
