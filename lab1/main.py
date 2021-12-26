# users = 4
# pswd len = 5
import os
import re

class User():
    def __init__(self, username, status, r, w, x, login, pswd) :
        self.name = username
        self.status = status
        self.login = login
        self.pswd = pswd
        self.r = r
        self.w = w
        self.x = x
        
user_list = []


def login(user_list) :
    authorized = False
    login = input('Login:')
    pswd = input('Password:')
    for user in user_list:
        if user.login == login and user.pswd == pswd :
            authorized = True
            current_user = user
            print('Authorized as', user.name)
            return authorized, current_user
        
    print('Login failure (wrong login or password)')
    return authorized, None

def pwd() :
    print(os.getcwd())
    return

def ls(path) :
    print(os.listdir(path))
    return

def cd(path, user) :
    abs_path = os.path.abspath(path)
    
    if user.status == 'admin' :
        os.chdir(path)
    elif abs_path.find(user.status) > 0 :
        os.chdir(path)
    else :
        print('You have no rights')
    return

def vi(path, user) :
    if user.w:
        with open(path, 'w') as file :
            text = input('Enter text: \n')
            file.write(text)
    else : 
        print('You have no rights')
    
    return

def mkdir(dir_name) :
    os.mkdir(dir_name)
    return

def rm(path_) :
    if os.path.isfile(path_) :
        os.remove(path_)
    elif os.path.isdir(path_):
        os.rmdir(path_)
    return

def logout() :
    return False, False

def main():
    
    root_user = User('root', 'admin', 1, 1, 1, 'root', '00000')
    user1 = User('user1', 'user', 1, 0, 1, 'user1', 'aaaaa')
    user2 = User('user2', 'user', 1, 0, 1, 'user2', 'bbbbb')
    user3 = User('user3', 'user', 1, 0, 1, 'user3', 'ccccc')
    user4 = User('user4', 'user', 1, 0, 1, 'user4', 'ddddd')
    user_list.append(root_user)
    user_list.append(user1)
    user_list.append(user2)
    user_list.append(user3)
    user_list.append(user4)

    cd_command = re.compile(r'(cd) (\w+|\.+)')
    mkdir_command = re.compile(r'(mkdir) (\w+)')
    rm_command = re.compile(r'(rm|rmdir) (\w+)')
    vi_command = re.compile(r'(vi) (\w+)')
    
    authorized = False
    authorized, curr_user = login(user_list)
    curr_path = os.chdir('lab1/root')
    
    while authorized :
        command = input()

        cd_cmd = cd_command.search(command)
        mkdir_cmd = mkdir_command.search(command)
        rm_cmd = rm_command.search(command)
        vi_cmd = vi_command.search(command)

        if command == 'pwd' :
            pwd()

        elif command == 'ls' :
            ls(curr_path)

        elif cd_cmd :
            cd(cd_cmd.group(2), curr_user)
            pwd()

        elif vi_cmd :
            vi(vi_cmd.group(2), curr_user)

        elif mkdir_cmd :
            mkdir(mkdir_cmd.group(2))

        elif rm_cmd :
            if os.path.exists(rm_cmd.group(2)) :
              rm(rm_cmd.group(2))

        elif command == 'logout' :
            authorized = False
            curr_user = None
    
    return

main()

