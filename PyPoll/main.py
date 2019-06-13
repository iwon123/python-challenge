def main():
	f = open("profit_loss.txt","w+")

	import os 
	import csv

	csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
	Candidate = []
	count = 0
	CA = 0
	CB = 0
	CC= 0
	CD = 0
	print('Election Results')
	print('--------------------------')
	with open(csvpath, newline = '') as election_data:
		data = csv.reader(election_data, delimiter = ',')
		header = next(data)
		print(header)

		for row in data:
			count = count + 1

			if row[2] not in Candidate:
				Candidate.append(row[2])

			if row[2] == Candidate[0]:
				CA = CA + 1
				CA_percentage = 100*(int(CA)/int(count))

			elif row[2] == Candidate[1]:
				CB = CB + 1
				CB_percentage = 100*(int(CB)/int(count))

			elif row[2] == Candidate[2]:
				CC = CC + 1
				CC_percentage = 100*(int(CC)/int(count))

			elif row[2] == Candidate[3]:
				CD = CD + 1
				CD_percentage = 100*(int(CD)/int(count))

		for i in Candidate: 
			if CA > CB and CC and CD:
				winner = Candidate[0]
			elif CB > CA and CC and CD:
				winner = Candidate[1]
			elif CC > CA and CB and CD:
				winner = Candidate[2]
			elif CD > CA and CB and CC:
				winner = Candidate[3] 


		print('Total Votes:' + str(count))
		print('--------------------------')
		print(f'{Candidate[0]} {str(round(CA_percentage,3))}% ({str(CA)})')
		print(f'{Candidate[1]} {str(round(CB_percentage,3))}%  ({str(CB)})')
		print(f'{Candidate[2]} {str(round(CC_percentage,3))}% ({str(CC)})')
		print(f'{Candidate[3]} {str(round(CD_percentage,3))}% ({str(CD)})')
		print('--------------------------')
		print(f'Winner: {winner}')
		print('--------------------------')

		f.write('Total Votes:' + str(count))
		f.write('--------------------------')
		f.write(f'{Candidate[0]} {str(round(CA_percentage,3))}% ({str(CA)})')
		f.write(f'{Candidate[1]} {str(round(CB_percentage,3))}%  ({str(CB)})')
		f.write(f'{Candidate[2]} {str(round(CC_percentage,3))}% ({str(CC)})')
		f.write(f'{Candidate[3]} {str(round(CD_percentage,3))}% ({str(CD)})')
		f.write('--------------------------')
		f.write(f'Winner: {winner}')
		f.write('--------------------------')


	f.close()


if __name__== "__main__":
	main()