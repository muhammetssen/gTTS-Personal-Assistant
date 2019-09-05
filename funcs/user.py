import json
database_path = './src/database/user_information.json'

class User:
    def __init__(self,name,age,city):
        with open(database_path , 'r') as database:
            data = eval(database.read())
            user_count = data['current_user_count']
        self.name = name
        self.age = age
        self.city = city
        self.user_id = user_count+1 
        data['current_user_count'] +=1
        data['user_'+str(self.user_id)] = {
            'user_id' : self.user_id,
            'name':self.name,
            'age':self.age,
            'city':self.city
        }
        open(database_path,'w').write(json.dumps(data))
    def __str__(self):
        return self.name
    @staticmethod
    def remove_user(user_id):
        with open(database_path , 'r') as database:
            data = eval(database.read())
        data['current_user_count'] -=1
        data.__delitem__(user_id)
        open(database_path,'w').write(json.dumps(data))
    @staticmethod
    def list_users():
        control = False
        while not control:
            try:
                var = int(input('Press 1 for detailed list \nPress 2 for just names\n'))
                if var not in [1,2]:
                    print('Please enter 1 or 0')
                    #var = int(input())
                else:
                    control = True
            except :
                print('Invalid')
        with open(database_path , 'r') as database:
            data = eval(database.read())
            data.__delitem__('current_user_count')
        if var == 1:
            for user in data.keys():
                print(data[user])
        elif var==2:
            for user in data.keys():
                print(data[user]['name'])
    


