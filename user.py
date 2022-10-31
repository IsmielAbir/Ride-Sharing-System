import hashlib

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
    
a = User('sb', 'ab@hh', 'hhjj')
User.log_in('ab@hh', 'hhjj') 