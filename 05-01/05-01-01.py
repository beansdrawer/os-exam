# 기본적인 파일 입출력 예제

with open("one_number.txt", "w") as f :
  f.write("one!")
  
with open("two_number.txt", "w") as f :
  f.write("two!")
  
with open("three_number.txt", "w") as f :
  f.write("three!")

import glob

for filename in glob.glob("*.txt", recursive=True):
  print(filename)

import fileinput

with fileinput.input(glob.glob("*.txt")) as fi:
  for line in fi :
    print(line)

import fnmatch
import os

for filename in os.listdir('.'):
  if fnmatch.fnmatch(filename, 'one_??????.txt'):
    print(filename)