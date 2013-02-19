#!/usr/bin/env python

_name = 'Turing Machine'
_version = '0.01'

from TuringMachine import *
import sys
import re

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Usage: run_turing.pu <program>"
    sys.exit(1)

  if sys.argv[1] == '-V':
    print "%s %s"%(_name, _version)
    sys.exit(0)

  data = sys.stdin.readline().rstrip()
  
  f = open(sys.argv[1],'r')
  reader = (line for line in (line[:line.find('#')%(len(line) +1)] for line in f) if line.strip('') != '')

  line = reader.next()
  fields = re.split('\s+', line.rstrip())
  
#  space_char = fields[0]
  finite_states = [int(field) for field in fields]

  m = TuringMachine(data, finite_states) 

  for line in reader:
#    print "add: %s"%line
    fields = re.split('\s+',line.rstrip())
    m.addTransition(int(fields[0]), fields[1], int(fields[2]), fields[3], fields[4])
  f.close()

  result = m.execute()
  if result != None:
    print result
  else:
    sys.exit(1)


