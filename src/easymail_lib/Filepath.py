#!/usr/bin/env python3
import os

class FilePath(object):
  def getSelectedFilepath(this):
    paths = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].splitlines()
    return paths

def main():
  filepath = FilePath()
  paths = filepath.getFilename()
  for p in paths:
    print(p)


if __name__ == "__main__":
  main()
