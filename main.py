#!/usr/bin/env python

import sys
import os.path
import re

def main(full_changelog, output):
	if not os.path.isfile(full_changelog):
		sys.exit("Input file doesn't exist")
	with open(full_changelog, 'r') as f, open(output, 'w') as out:
		matching = False
		for line in f:
			if re.search('\|\ \d\.\d\.\d$', line):
				if matching:
					print("Wrote changelog to", output)
					return
				matching = True
			if matching:
				if not line.isspace():
					out.write(line)
	sys.exit("Couldn't write changelog")

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
