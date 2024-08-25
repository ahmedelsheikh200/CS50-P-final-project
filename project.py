import pycountry
import csv
class Person:
    def __init__(self,first_name,last_name,country,age,rating):
        self.first_name=first_name
        if  first_name =="":
            raise ValueError ("Not a valid name.")
        self.last_name=last_name
        if  last_name =="":
            raise ValueError ("Not a valid name.")
        self.country= country
        self.age=age
        if age <= 0 :
            raise ValueError ("Not a valid age.")
        self.rating=rating
        if rating < 0 :
            raise ValueError ("Not a valid rating.")
class User(Person):
    def __init__(self,first_name,last_name,country,age,rating):
        super().__init__(first_name,last_name,country,age,rating)
    def __str__(self):
            return f"user's name is {self.first_name} {self.last_name}, he is from {self.country},he is {self.age} years old, and his rating is {self.rating}"




    @staticmethod
    def get_user():
        first_name=input("enter your first name :").strip()
        last_name=input("enter your last name :").strip()
        # Get user input
        while True:
            user_country = input("Enter your country: ")
            try:
                country = pycountry.countries.lookup(user_country)
                country=user_country
                break
            except LookupError:
                print("Not a valid country. Please try again.")
        age = int(input("Enter your age :"))

        rating = int(input("Enter your rating: "))
        return User(first_name, last_name, country, age, rating)


class Coach(Person):
    def __init__(self, first_name,last_name,country ,age,rating,experience_years):
        super().__init__(first_name,last_name,country,age,rating)
        self.experience_years = experience_years
        if experience_years < 0:
            raise ValueError("Not Valid")
    def __str__(self):
            return f"user's name is {self.first_name} {self.last_name}, he is from {self.country},he is {self.age} years old, and his rating is {self.rating} and he has {self.experience_years} yeras as a coach"

    @staticmethod
    def get_coach():
        first_name=input("enter your first name :").strip()
        last_name=input("enter your last name :").strip()
        # Get user input
        while True:
            user_country = input("Enter your country: ")
            try:
                country = pycountry.countries.lookup(user_country)
                country=user_country
                break
            except LookupError:
                print("Not a valid country. Please try again.")
        age = int(input("Enter your age :"))

        rating = int(input("Enter your rating: "))
        experience_years = int(input('years of wrking as a coach:'))
        return Coach(first_name,last_name, country,age, rating,experience_years)


def main():
    friend = know_the_user()
    if friend == "t":
        print("welcome"'\n'"here you will find the best coaches")
        save_students_data(friend)
        print("saved")
        print("enjoy your journey and choose your coach")
        choose_coach()
    if friend == "c":
        print("welcome"'\n'"here you will find a job and help students")
        save_coaches_data(friend)

def know_the_user(user_input=None):
    if user_input is None:
        while True:
            friend = input("If you are a coach type 'c', if you are a trainee type 't': ").strip().lower()
            if friend in ["c", "t"]:
                return friend
    else:
        if user_input in ["c", "t"]:
            return user_input
        else:
            return None


def save_students_data(u):
    user = User.get_user()
        # Write user data to CSV file
    with open('students.csv', 'a', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Country', 'Age', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty, write header if needed
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'First Name': user.first_name.capitalize(),
            'Last Name': user.last_name.capitalize(),
            'Country': user.country,
            'Age': user.age,
            'Rating': user.rating
        })
    ...


def save_coaches_data(i, coach_data=None):
    if coach_data is None:
        # Get coach data
        coach = Coach.get_coach()
    else:
        coach = coach_data

    # Write coach data to CSV file
    with open('coaches.csv', 'a', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Country', 'Age', 'Rating', 'experience Years' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty, write header if needed
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'First Name': coach.first_name.capitalize(),
            'Last Name': coach.last_name.capitalize(),
            'Country': coach.country,
            'Age': coach.age,
            'Rating': coach.rating,
            'experience Years': coach.experience_years
        })

def choose_coach():
    # Read coach data from CSV file
    coaches = []
    with open('coaches.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            coaches.append(row)

    # Display coaches
    print("Available Coaches:")
    for i, coach in enumerate(coaches):
                print(f"{i + 1}. {coach['First Name']} {coach['Last Name']}, {coach['Country']}, Age: {coach['Age']}, Rating: {coach['Rating']}")

    # Ask user to choose a coach
    while True:
        try:
            choice = int(input("Choose a coach by entering its number: "))
            if 1 <= choice <= len(coaches):
                chosen_coach = coaches[choice - 1]
                print(f"You've chosen {chosen_coach['First Name']} {chosen_coach['Last Name']}.")
                return chosen_coach
            else:
                print("Invalid choice. Please enter a valid coach number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()


