#!/usr/bin/env python

import sys
import os.path

def main(full_changelog, output, separator='*****'):
	if not os.path.isfile(full_changelog):
		sys.exit("Input file doesn't exist")
	with open(full_changelog, 'r') as f, open(output, 'w') as out:
		lines = f.readlines()
		for line in lines:
			if line.strip() == separator:
				print("Wrote changelog to", output)
				return
			if not line.isspace():
				out.write(line)
	print("Wrote changelog to", output)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '*****')
