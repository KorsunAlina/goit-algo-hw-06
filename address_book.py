from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass 
        

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
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value==phone:
                return p
            else:
                raise ValueError("Phone number not found.")
        return None    
    
    def remove_phone(self, phone_number):
        phone=self.find_phone(phone_number)
        self.phones.remove(phone)       
    
    def edit_phone(self, phone, new_phone):
        old = self.find_phone(phone)
        if old:
            self.remove_phone(old.value)
            self.add_phone(new_phone)
            return True
        return False

           
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value]=record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        self.data.pop(name, None)
            
    
    def __str__(self):
        if not self.data:
            return "AddressBook is empty."
        
        result = []
        for record in self.data.values():
            phones = ", ".join(p.value for p in record.phones)
            result.append(f"Name: {record.name.value}\nPhones: {phones}")
        return "\n\n".join(result)
    
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223339")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
