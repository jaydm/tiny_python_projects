#!/usr/bin/env python
# Purpose: Say hello

import sys

def usage(message:str = 'Program run without any arguments') -> None:
  print(message + '\nusage: hello.py NAME')

def greet(name:str = 'World') -> str:
  return f'Hello, {name}!'

def test_greet() -> None:
  assert greet() == 'Hello, World!'
  assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
  if len(sys.argv) == 1:
    usage()
    sys.exit(1)
  elif len(sys.argv) > 2:
    usage('Program called with too many arguments')
    sys.exit(1)
  
  print(greet(sys.argv[1]))
  
if __name__ == '__main__':
  main()
