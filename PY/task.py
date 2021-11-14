'''
class Blood:
    def __init__(self,gun,bullet,bulletspeed):
        self.gun = gun
        self.bullet = bullet    
        self.bulletspeed = bulletspeed
    
    def gunsound(self,sound):
        print("Diskin Diskin")
        
    def info(self):
        print("GunModel: ", self.gun)
        print("Bullet: ", self.bullet)
        print("BulletSpeed: ", self.bulletspeed)
        
GunInfo = Blood("AK-47",7.62, 745)
GunInfo.info()
GunInfo.kill("Enemy")
'''

class User:
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password
        
    def info(self):
        print("Username:", self.Username)
        print("Password:", self.Password)
        

class Moderator(User):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)
        
    def Ban(self, Ban_name):
        print(Ban_name, "Banned!")
        

mod1 = Moderator("Elman", "Admin321")
mod1.info()
mod1.Ban(input("Please Enter Name To Ban: "))

class Admin(Moderator):
    def __init__(self, Username, Password, ID, PIN):
        super().__init__(Username, Password)
        self.ID = ID
        self.PIN = PIN
        
    def Admininfo(self, Account_Delete):
        print(Account_Delete, "Account Succesfully Deleted!")
        
admin1 = Admin("Elmanms", "Elmnadmin", "E123", "1223")
admin1.Admininfo(input("Enter Account: "))