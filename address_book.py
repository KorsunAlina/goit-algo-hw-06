from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name) 
        

class Phone(Field):
    def __init__(self, phone):
        if not phone.isdigit() or len(phone)!=10:
            raise ValueError("The number must have 10 digits!")
        super().__init__(phone)
        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone=Phone(phone_number)
        self.phones.append(phone)
        
    def remove_phone(self, phone_number):
        phone=Phone(phone_number)
        self.phones.remove(phone)
    
    def edit_phone(self, phone, new_phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Incorrect phone number that you want to edit!")
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("Incorrect new phone number!")

        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones[i] = Phone(new_phone)
                return True
        raise ValueError("The phone you try to change does not exist!")

    def find_phone(self, phone):
        for p in enumerate(self.phones):
            if p.value==phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[Record.name.value]=record

    def find(self, name):
        for record in self.data.values:
            if record.name.value==name:
                return record
        return None 
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"The user {name} is deleted successfully!"
        return "The user you try to delete is not exist!"
    
    def __str__(self):
        if not self.data:
            return "AddressBook is empty."
        
        result = []
        for record in self.data.values():
            phones = ", ".join(p.value for p in record.phones)
            result.append(f"Name: {record.name.value}\nPhones: {phones}")
        return "\n\n".join(result)