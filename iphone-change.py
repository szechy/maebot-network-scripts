#!/usr/bin/python

def main():
  interfaces = open("/etc/network/interfaces", "wb")
  print "Name: ", interfaces.name
  pass

if __name__ == "__main__":
  main()
