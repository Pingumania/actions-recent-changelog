#!/usr/bin/env python

import sys
import os.path

def main(full_changelog, output, separator='*****'):
	if not os.path.isfile(full_changelog):
		sys.exit("Input file doesn't exist")
	with open(full_changelog, 'r') as f:
		lines = f.readlines()
	kept = []
	for line in lines:
		if line.strip() == separator:
			break
		if not line.isspace():
			kept.append(line)
	with open(output, 'w') as out:
		out.writelines(kept)
	print("Wrote changelog to", output)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '*****')
