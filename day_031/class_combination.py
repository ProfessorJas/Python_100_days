class Person(object):           # Define a Person class
    def __init__(self, name, age, gender, birthday, address, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.address = address
        self.contact = contact

    def printBaseInformation(self):
        print('Basic Info.: Name: %s, Age: %s, Gender: %s' % (self.name, self.age, self.gender))

    def printBirthdayInfo(self):
        print('Birthday: %s-%s-%s' % (self.birthday.year, self.birthday.month, self.birthday.day))

    def printAllInfo(self):
        # Call methods in Person class
        self.printBaseInformation()

        # Call methods in Birthday class
        self.printBirthdayInfo()
        
        # Call methods in Address class
        self.address.printAddressInfo()

        # Call methods in Contact class
        self.contact.printContactInfo()

class Birthday(object):
    # Define a Birthday class
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Address(object):
    # Define an Address class
    def __init__(self, nation, province, city, region, street):
        self.nation = nation
        self.province = province
        self.city = city
        self.region = region
        self.street = street

    # Define method printAddressInfo
    def printAddressInfo(self):
        print('Address: %s, %s, %s, %s, %s' % (self.nation, self.province, self.city, self.region, self.street))

class Contact(object):
    # Define a Conact class
    def __init__(self, telephone, wechat, qq):
        self.telephone = telephone
        self.wechat = wechat
        self.qq = qq

    def printContactInfo(self):
        print('Contact Info: Tel.: %s, WeChat: %s, QQ: %s' % (self.telephone, self.wechat, self.qq))

# Create a Birthday object birthday
birthday = Birthday(2000, 1, 1)

# Create an Address object address
address = Address('China', 'Shanghai', 'Shanghai', 'Xuhui', 'Hengshan Road')

# Create a Contact objet contact
contact = Contact('123456789', '789789jaja', '7777777')

person = Person('An Amigo', '17', 'Male', birthday, address, contact)

person.printAllInfo()