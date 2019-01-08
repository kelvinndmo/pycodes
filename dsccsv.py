import csv

class ReadDsc:
    
    def WriteContact(self):
        with open('k.csv', 'r') as novak:
            csv_reader = csv.DictReader(novak)

            with open('kevo.csv', 'w') as vero:
                fieldnames = ["Username"]
                
                csv_writer = csv.DictWriter(vero, fieldnames=fieldnames, delimiter='\t')

                csv_writer.writeheader()

                for line in csv_reader:
                  del line['Timestamp']
                  del line['Gender']
                  del line['Phone Number']
                  del line["Are you willing to commit a minimum of 1 hr every Thursday to learn and work on technical projects?"]
                  del line["What is your proficiency in coding?"]
                  del line["Official Name"]
                  del line["Course"]
                  del line["Year of Study"]
                  csv_writer.writerow(line)



ReadDsc = ReadDsc()
ReadDsc.WriteContact()