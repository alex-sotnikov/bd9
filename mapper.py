def map(record):
	ipaddress, bannerid, country, userid, payment = record.split(",")
	payment=float(payment)
	yield country, payment