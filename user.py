import hashlib
from brta import BRTA

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as f:
            f.write(f'{email} {pwd}')
        f.close()
        print(self.name, 'user created')

    
    
    @staticmethod
    def log_in(email, password):  
        stored_pass = ''
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if email in line:
                    stored_pass = line.split(' ')[1]
                      
        f.close()
        hash_pwd = hashlib.md5(password.encode()).hexdigest()
        if hash_pwd == stored_pass:
            print('Valid user')
            return True
        else:
            print('Invalid user')
            return False
        print('Password found', stored_pass)



class Rider(User):
    def __init__(self,name, email, password, location, balance):
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)
        
    def set_location(self, location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        pass
    
    def start_a_trip(self, fare):
        self.balance -= fare




class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        
        
        
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry you failed, try again')
        else:
            self.license = result
            self.valid_driver = True
        
        
        
        
    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination



   
userab = User('sb', 'ab@hh', 'hhjj')
User.log_in('ab@hh', 'hhjj') 

kuber = Driver('kuber', 'kuber@.com', 'kopila', 54, 4554)

result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
kuber.take_driving_test()