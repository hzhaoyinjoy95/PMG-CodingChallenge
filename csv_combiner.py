import csv
import sys              

def merge_csv():
    #A function developed to combine n csv files

    #create empty list to hold data
    all_content = []
    #create a header
    all_content.append(['email_hash','category','filename'])

    #loop through arguments to extract information
    for i in range(len(sys.argv)-1):
        with open(sys.argv[i+1],'r') as csvinput:
            #skip the original header
            next(csvinput)
            filename = sys.argv[i+1].split('/')[-1].split('.')[0]
            #read in information after header
            reader = csv.reader(csvinput)
            
            #loop line by line to add/extract information to avoid running out of memory
            for row in reader:
                row.append(filename)
                all_content.append(row)
        
    #write to stdout    
    writer = csv.writer(sys.stdout)
    writer.writerows(all_content)

if __name__ == '__main__':
    merge_csv()
    