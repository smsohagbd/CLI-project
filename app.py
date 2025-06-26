import csv
import sys



class Handle_csv:
    outputfile = 'contacks.csv'

    def add_data(self):
        name = input('Enter Name: ').strip()
        phone = input('Enter Phone Number : ').strip()
        email = input('Enter Email : ').strip()
        address = input('Enter Address : ').strip()
        found = False

        with open(self.outputfile, 'r') as file:
            reader = csv.reader(file)
            for re in reader:
                if re and re[1].strip() == phone:
                    found = True
                    break
        if found:
            print('Error: Phone number already exists for another contact.')

        else:
            if not name:
                print('Your name is required : ')
                return
            elif not name.isalpha():
                print('The contact’s name must be a string.')
                return
            elif not phone:
                print('Your Phone is required : ')
                return
            elif not phone.isdigit():
                print('The phone number must be an integer.')
                return
            elif not email:
                print('Your Email is required : ')
                return
            elif '@' not in email or not email.endswith('.com') :
                print('Invalid Email Address')
                return
            elif not address:
                print('Your Address is required : ')
                return
            else:
                with open(self.outputfile , 'a' , newline='') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([name , phone , email , address])
                print('Contact added successfully!')
        
    def read_data(self):        
            print('===== All Contacts =====')
            for i , re in enumerate(self.data , 1):
              print(f"{i}.Name : {re[0]} \n Phone: {re[1]}\n Email : {re[2]}\n Address : {re[3]}")

    def delete_data(self):
        phone = input('Enter the phone number of the contact to delete: ').strip()
        confim = input(f'Are you sure you want to delete contact numbers {phone}? (y/n): ').strip().lower()
        data_found = []
        deleted = False
        found = False
        with open(self.outputfile , 'r', encoding='utf-8') as file:
            read_data = csv.reader(file)
            for read in read_data:
                if read and read[1].strip() == phone:
                    found = True
                    if confim == 'y':
                        deleted = True
                        print('Contact deleted successfully!')
                        continue 
                    else:
                        data_found.append(read)
                        print('Delete canceled')
                else:
                    data_found.append(read)

        if not found:
            print('No matching phone number found.')

        with open(self.outputfile , 'w', newline='') as file:
            delete_user_data = csv.writer(file)
            delete_user_data.writerows(data_found)

    def search_data(self):
        name = input('Enter search term (name/email/phone): ').strip().lower()
        found = False

        for search in self.data:           
            if search and search[0].lower().strip() == name or search[1].lower().strip() == name or search[2].lower().strip()  == name:
                found = True
                print(f"Search Result: \nName : {search[0]} \nPhone : {search[1]}\nEmail : {search[2]}\nAddress : {search[3]}")
        
        if not found:
            print('Your information not listed')        

    def load_contact(self):
        self.data = []
        with open(self.outputfile , 'r') as file:
            reader = csv.reader(file)
            for read in reader:
                self.data.append(read)
            





model = Handle_csv()
while True:
    try:
        print('\nWelcome to the Contact Book CLI System!')
        model.load_contact()
        print('Loading contacts from contacts.csv... Done!')
        print('1. Add Contact')
        print('2. Search Contact')
        print('3. View All Contacts')
        print('4. Remove Contact')
        print('5. Exit')
        print('===============================')

        choose = input('Enter your choose: ')
        if choose == '1':
            model.add_data()
        elif choose == '2':
            model.search_data()
        elif choose == '3':
            model.read_data()
        elif choose == '4':
            model.delete_data()
        elif choose == '5':
            print('Thank you for using the Contact Book CLI System. Goodbye!')
            sys.exit()
        else:
            print('Please Put Number 1 to 5')

    except Exception as e:
        print('Error : ' , str(e))