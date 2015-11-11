#!/usr/bin/env python3
import os

class FilePath(object):
  def getSelectedFilepath(self):
    paths = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', None)

    if paths is not None:
      return self.toDoubleArray(paths)
    return paths

  def toDoubleArray(self, paths):
    if paths is not None:
      paths = paths.splitlines()
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
  paths = filepath.getSelectedFilepath()
  for p in paths:
    print(p)


if __name__ == "__main__":
  main()
