import pickle

class AddressBook:
    def __init__(self):
        email_set = set()
        mobile_set = set()
        FName_list = []
        LName_list = []
        street_list = []


    def add_data(self, FName, LName, StreetAddress, City, State, Country, Mobile, email):
        self.email_set.add(email)
        self.mobile_set.add(Mobile)
        self.FName_list.append(FName)
        self.LName_list.append(LName)
        self.street_list.append(StreetAddress)
        print("Successfully added the person")

    #     def count_occurrences(self, field):
    #         if field == "Fname":
    #             FName_input=input("Enter FName: ")
    #             print ("The no.of occurences of {} is {}".format(FName_input, self.FName_list.count(FName_input)))
    #         elif field == "LName":
    #             LName_input=input("Enter LName: ")
    #             print ("The no.of occurences of {} is {}".format(LName_input, self.LName_list.count(LName_input)))
    #         elif field == "StreetAddress":
    #             street_input=input("Enter street: ")
    #   print ("The no.of occurences of {} is {}".format(street_input, self.street_list.count(street_input)))
    def save_data(self, file_path):
        data = {'mobile': self.mobile_set, 'email': self.email_set, 'Fname': self.FName_list, 'LName': self.LName_list,
                'street': self.street_list}
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = pickle.load(f)
                self.email_set = data.get('email', set())
                self.mobile_set = data.get('mobile',set())
                self.FName_list = data.get('Fname',[])
                self.LName_list = data.get('Lname',[])
                self.street_list = data.get('street',[])
        except FileNotFoundError:
            self.email_set = set()
            self.mobile_set = set()
            self.FName_list = []
            self.LName_list = []
            self.street_list = []

    def FName_Occurences(self):
        FName_input = input("Enter FName: ")
        print("The no.of occurences of {} is {}".format(FName_input, self.FName_list.count(FName_input)))

    def LName_Occurences(self):
        LName_input = input("Enter LName: ")
        print("The no.of occurences of {} is {}".format(LName_input, self.LName_list.count(LName_input)))

    def Street_Occurences(self):
        street_input = input("Enter street: ")
        print("The no.of occurences of {} is {}".format(street_input, self.street_list.count(street_input)))


book = AddressBook()
book.load_data('problem2_data_file.pickle')

while True:
    user_input = input("""
        What do you want to do
        1. Enter 1 to add a person
        2. Enter 2 to find the number of occurrences of a FName
        3. Enter 3 to find the number of occurrences of a LName
        4. Enter 4 to find the number of occurrences of a street
        5. Enter 5 to quit
        """)

    if user_input == '1':
        FName = input("Enter FName: ")
        LName = input("Enter LName: ")
        StreetAddress = input("Enter Street Address: ")
        City = input("Enter City: ")
        State = input("Enter State: ")
        Country = input("Enter Country: ")
        Mobile = input("Enter Mobile no: ")
        email = input("Enter Email: ")

        if email in book.email_set or Mobile in book.mobile_set:
            print("email or mobile already exists, try again")
            continue
        else:
            book.add_data(FName, LName, StreetAddress, City, State, Country, Mobile, email)

    elif user_input == '2':
        book.FName_Occurences()
    #         book.count_occurrences(self,"FName" )
    elif user_input == '3':
        book.LName_Occurences()
    #         book.count_occurrences(self,"LName" )
    elif user_input == '4':
        book.Street_Occurences()
    #         book.count_occurrences(self,""StreetAddress"" )
    elif user_input == '5':
        book.save_data('problem2_data_file.pickle')
        print('Goodbye')
        break
    else:
        print("invalid input, try again")