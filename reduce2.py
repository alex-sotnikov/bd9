#!/opt/anaconda/envs/bd9/bin/python
import sys

def main():
	last_country = None
	count = 0
	sum_all = 0
	for line in sys.stdin:
		country, payment = line.strip().split("\t")
		if last_country is None:
			last_country = country
			count += 1
			sum_all += float(payment)
		elif country == last_country:
			count +=1
			sum_all += float(payment)
		else:
			sys.stdout.write("{0}, {1}\n".format(last_country, float(sum_all)))
			last_country = country
			count = 1
			sum_all = float(payment)
	sys.stdout.write("{0}, {1}\n".format(last_country, float(sum_all)))

if __name__ == "__main__":
	main()