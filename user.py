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
        
        
    
    
    
    
