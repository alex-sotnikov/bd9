#!/opt/anaconda/envs/bd9/bin/python
import sys

def main():
    for line in sys.stdin:
		ipaddress, bannerid, country, userid, payment = line.split(",")
		payment=float(payment)
		sys.stdout.write("{0}\t{1}\n".format(country, payment))


if __name__ == "__main__":
    main()