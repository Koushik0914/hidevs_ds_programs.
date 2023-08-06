# Problem 1
# a) Write a class which takes input from the console name of
# the person and his/her date of birth. Then when the person’s name is typed it should display the dob.
# b) Some person's dob is secret so those should not be displayed,
# but will be stored. If a secret person's name is entered, you should just display “secret”.
# However, all the data should be persisted, and loaded. We can add it to the list.
# What data structure would you create for these two problems?
# File contains:-
# problem1_data_file.pickle => Entered data will be saved in that file.
# problem1_solution.py => Solution code of problem1 statement.

import pickle


class BirthdayTracker:
    def __init__(self):
        self.birthdays = {}
        self.secret_names = set()

    def add_birthday(self, name, dob, is_secret=False):
        if is_secret:
            self.secret_names.add(name)
        else:
            self.birthdays[name] = dob

    def get_birthday(self, name):
        if name in self.secret_names:
            return "Secret"
        return self.birthdays.get(name, "Birthday not found for this name.")

    def save_data(self, file_path):
        with open(file_path, 'wb') as f:
            data = {'birthdays': self.birthdays, 'secret_names': self.secret_names}
            pickle.dump(data, f)

    def load_data(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = pickle.load(f)
                self.birthdays = data.get('birthdays', {})
                self.secret_names = data.get('secret_names', set())
        except FileNotFoundError:
            # In case if the file doesn't exits
            self.birthdays = {}
            self.secret_names = set()

tracker = BirthdayTracker()
# load data
tracker.load_data('problem1_data_file.pickle')

while True:
    print("1. Add a person's birthday")
    print("2. Retrieve a person's birthday")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter the person's name: ")
        dob = input("Enter the person's date of birth (YYYY-MM-DD): ")
        is_secret = input("Is this person's birthday a secret? (yes/no): ")
        tracker.add_birthday(name, dob, is_secret == "yes")
        print("Birthday added for", name)
    elif choice == "2":
        name = input("Enter the person's name: ")
        dob = tracker.get_birthday(name)
        print(f"{name}'s date of birth is: {dob}")
    elif choice == "3":
        # Save data to the file before exiting
        tracker.save_data('problem1_data_file.pickle')
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")

