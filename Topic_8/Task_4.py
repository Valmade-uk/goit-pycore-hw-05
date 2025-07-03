def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot. Type 'exit', 'close', or 'good bye' to quit.")

    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ['exit', 'close', 'good bye']:
            print("Good bye!")
            break
        elif command.startswith("add"):
            parts = command.split()
            result = add_contact(parts[1:], contacts)
            print(result)
        elif command.startswith("change"):
            parts = command.split()
            result = change_contact(parts[1:], contacts)
            print(result)
        elif command.startswith("phone"):
            parts = command.split()
            result = get_phone(parts[1:], contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()