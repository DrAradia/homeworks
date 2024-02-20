def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "There's no contact by that name. You can start by adding a contact."
        except IndexError:
            return "There's no contact by that name." 
        except Exception as e:
            return f"Exception {e}"
    return inner 

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise(KeyError)
    
def show_all(contacts):
    return contacts  

@input_error    
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]         

@input_error
def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))  
        elif command == "all":
            print(show_all(contacts))   
        elif command == "phone":
            print(show_phone(args, contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()