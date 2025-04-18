#!/usr/bin/env python

import sys
import os.path
import re

def main(full_changelog, output):
	if not os.path.isfile(full_changelog):
		sys.exit("Input file doesn't exist")
	with open(full_changelog, 'r') as f, open(output, 'w') as out:
		matching = False
		lines = f.readlines()
		for line in lines:
			if re.search('^.* \| .*$', line):
				if matching:
					print("Wrote changelog to", output)
					return
				matching = True
			if matching:
				if not line.isspace():
					out.write(line)
				if line is lines[-1]:
					print("Wrote changelog to", output)
					return
	sys.exit("Couldn't write changelog")

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
