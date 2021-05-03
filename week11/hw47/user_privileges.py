################################################################################
# Author: Fanyang Cheng
# Date: 04/15/2021
# Description:This program could let the user build a system with users' email
# and the privileges and add/remove/get those privileges.
################################################################################
#define class privileges
class Privileges():
    def __init__(self,privs = {'interact','post'}):
        self.privs = set(privs)
    def grant(self,string):
        self.privs.add(string)
        print('Granted',string)
    def revoke(self,string):
        self.privs.remove(string)
        print('Revoked',string)
    def get_privs(self):
        return(', '.join(sorted(i for i in self.privs))) # return them in separation of ','

#define class user
class User():
    def __init__(self,name,email):
        self.privs = Privileges()
        self.name = name
        self.email = email
    def describe_user(self):
        print('User Profile')
        print('  Name:',self.name)
        print('  Email:',self.email)
        print('  Privs:',', '.join(sorted(i for i in self.privs.privs)))

def main():
    #define a user called Alice
    privs = Privileges()
    Ali = User('Alice','alice@example.com')
    Ali.privs = privs
    Ali.describe_user()
    privs.grant('teleport')
    Ali.describe_user()
    privs.revoke('post')
    Ali.describe_user()


if __name__ == '__main__':
    main()
