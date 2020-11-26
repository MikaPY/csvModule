import csv 

with open("new_info.csv", 'r') as csv_f:
	csv_r = csv.DictReader(csv_f)

	for line in csv_r:
		print(line)




	# with open('new_info.csv', 'w') as n_file:
	# 	csv_w = csv.writer(n_file, delimiter="\t")


	# 	for line in csv_r:
	# 		csv_w.writerow(line)
		
