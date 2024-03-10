from collections import UserDict
from datetime import datetime, timedelta

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e)=="wrong date":
                return f"Invalid date format. Use DD.MM.YYYY"
            return "You haven't entered a value. Nothind to add/change."
        except KeyError:
            return "There's no contact by that name. You can start by adding a contact."
        except IndexError:
            return "There's no contact by that name." 
        except Exception as e:
            return f"Exception {e}"
    return inner      

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return str(self.value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
    
    def validate(self):
        if len(self.value) == 10 and self.value.isdigit():
            return True
        return False

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("wrong date")            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.birthday = None

    def add_phone(self, phone):
        self_phone_input = Phone(phone)
        if self_phone_input.validate():
            self.phone=str(self_phone_input)
        else:
            print("Invalid phone. Phone number should be 10 digits.")
            self.phone='No phone'

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {self.phone}"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)       

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    # def delete(self, name):
    #     return self.data.pop(name, None)
    
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date()
                birthday_this_year = datetime(year=today.year, month=birthday_date.month, day=birthday_date.day).date()
                if birthday_this_year < today:
                    birthday_this_year = datetime(year=today.year+1, month=birthday_date.month, day=birthday_date.day).date()
                week_day = birthday_this_year.isoweekday()
                days_between = (birthday_this_year - today).days
                if 0 <= days_between <= 7:
                    if week_day <= 5:
                        upcoming_birthdays.append({'name': record.name.value, 'birthday': birthday_this_year.strftime("%Y.%m.%d")})
                    else:
                        if (birthday_this_year + timedelta(days=1)).weekday() == 0:
                            upcoming_birthdays.append({'name': record.name.value, 'birthday': (birthday_this_year + timedelta(days=1)).strftime("%Y.%m.%d")})
                        elif (birthday_this_year + timedelta(days=2)).weekday() == 0:
                            upcoming_birthdays.append({'name': record.name.value, 'birthday': (birthday_this_year + timedelta(days=2)).strftime("%Y.%m.%d")})

        return upcoming_birthdays
    
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
# по факту не дуже має сенс, так як за прикладом з дз add_contact для відомого контакту виконує ту ж функцію? 
def change_contact(args, book):
    name, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.add_phone(new_phone)
        return "Contact updated."
    else:
        raise(KeyError)

@input_error
def show_all(book):
    contacts = []
    for name, record in book.data.items():
        contacts.append(str(record))
    return "\n".join(contacts)

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return f"{record.name}: {record.phone}"
    else:
        raise(KeyError)

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise(KeyError)

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return f"{record.name}: {record.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"{record.name}: Birthday not set."
    else:
        raise (KeyError)

@input_error
def birthdays(args, book):
    return book.get_upcoming_birthdays()

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            birthdays_list = birthdays(args, book)
            if birthdays_list:
                for birthday in birthdays_list:
                    print(f"{birthday['name']}: {birthday['birthday']}")
            else:
                print("No upcoming birthdays.")

        else:
            print("Invalid command.")
            

if __name__ == "__main__":
    main()