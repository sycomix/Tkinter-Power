#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Noname400
"""

from bloomfilter import BloomFilter
import sys


def count_lines(file):
	return sum(1 for _ in open(file, 'r'))


def add_to_bf(file, nom, bf_filter):
	i = 0
	line_10 = 100000
	with open(file) as f:
		while i < nom:
			if line_10 == i:
				print(f"Total line ->{str(line_10)}", end='\r')
				line_10 += 100000
			text = f.readline().strip()
			if text[:2] == '0x': bf_filter.add(text.lower()[2:])
			else: bf_filter.add(text)
			i += 1


def bloom_filter():
	print("[I] Bloom Filter START")
	print(f"[I] File input -> {file_txt}")
	print(f"[I] File output -> {file_bf}")
	bf = BloomFilter(size=line_count, fp_prob=1e-16)

	print("[I] ADD Bloom Filter")
	add_to_bf(file_txt, line_count, bf)

	# Print several statistics of the filter
	print("[I] Bloom Filter Statistic")
	print(
		f"[+] Capacity: {bf.size} item(s)",
		f"[+] Number of inserted items: {len(bf)}",
		f"[+] Filter size: {bf.filter_size} bit(s)",
		f"[+] False Positive probability: {bf.fp_prob}",
		f"[+] Number of hash functions: {bf.num_hashes}",
		f"[+] Input file: {file_txt}",
		f"[+] Output file: {file_bf}",
		sep="\n",
		end="\n\n",
	)

	# Save to file
	print("[I] Bloom Filter Start Save File")
	with open(file_bf, "wb") as fp:
	    bf.save(fp)
	print("[I] Bloom Filter END Save File")


if __name__ == "__main__":

	if len (sys.argv) < 3:
	    print ("Ошибка. Слишком мало параметров.")
	    sys.exit (1)

	if len (sys.argv) > 3:
	    print ("Ошибка. Слишком много параметров.")
	    sys.exit (1)

	file_txt = sys.argv[1]
	file_bf = sys.argv[2]

	line_count = count_lines(file_txt)
	print(f"all lines -> {str(line_count)}")
	bloom_filter()
