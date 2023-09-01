class user:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('user created!')

    
user1 = user('prajwal', 'prajwal s', 'prajwal@example.com')

print(user1.name)

# print('username:{}, name: {}, email:{}'.format(user1.username, user1.name, user1.email))