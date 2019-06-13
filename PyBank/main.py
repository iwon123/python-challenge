def main():
	f = open("profit_loss.txt","w+")

	import os
	import csv
	import re
	#open the data file 
	csvpath = os.path.join('..','PyBank','Resources', 'budget_data.csv')
	profit_loss = []
	count = 0
	before = 0
	changes = []
	maxvalue = 0
	minvalue = 0
	print('Finacial Analysis')
	print('----------------------------------------')
	with open(csvpath, newline ='') as budget_file:
	    lines = csv.reader(budget_file, delimiter =(','))
	    header = next(lines)
	 
	    for row in lines:
	    	#print(row)
	    	#find the total of months
	    	count = count + 1
	    	# find the total 
	    	profit_loss.append(int(row[1]))
	    	total = (sum(profit_loss))
	    	#find the average changes
	    	difference = int(row[1]) -(before)
	    	before = int(row[1])
	    	changes.append(difference)
	    	# to get the date corresponding to the max and min value
	    	if difference > maxvalue:
	    		maxvalue = difference
	    		maxdate = row[0]

	    	if difference < minvalue:
	    		minvalue = difference
	    		mindate = row[0]


	    average = (sum(changes[1:]))/(count - 1)
	    #print(average) # to check
	    #print(changes) # to check
	    #print(max(changes)) # to check
	    #print(min(changes)) # to check
	    print('Total Months: ' + str(count))
	    print(f'Total:  ${str(total)}')
	    print(f'Average Change: ${str(round(average,2))}')
	    print(f'Greatest Increase in Profits: {maxdate} (${max(changes)})')
	    print(f'Greatest Decrease in Profits: {mindate} (${min(changes)})')
	    f.write(f'Total Months: {str(count)} \n') 
	    f.write(f'Total:  ${str(total)}')
	    f.write(f'Average Change: ${str(round(average,2))}')
	    f.write(f'Greatest Increase in Profits: {maxdate} (${max(changes)})')
	    f.write(f'Greatest Decrease in Profits: {mindate} (${min(changes)})')

	f.close()


if __name__== "__main__":
	main()


   
