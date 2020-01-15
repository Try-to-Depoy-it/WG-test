import os
#os.system('pip3 install gitpython')

import git, shutil

# create local Repo/Folder
if os.name == 'nt':
    UPLOAD_FOLDER = os.environ['OLDPWD'] + '%USERPROFILE%\Desktop\python1_test'
    #UPLOAD_FOLDER = "C:\python_test"
else:
    UPLOAD_FOLDER = os.environ['OLDPWD'] + '/python1_test'

new_path = os.path.join(UPLOAD_FOLDER)

#print (new_path)

NAME = new_path
URL = 'https://github.com/Darth-Kordis/python_test.git'
BRANCH: str = 'another-new-one'

class git_operations():
    def __init__(self, name, url, branch):
        self.DIR_NAME = name
        self.REMOTE_URL = url
        self.NEW_BRANCH = branch

    def git_clone(self):
        try:
            if not os.path.exists(self.DIR_NAME):
                if os.path.isdir(self.DIR_NAME):
                    shutil.rmtree(self.DIR_NAME)
                os.mkdir(self.DIR_NAME)
                print(self.DIR_NAME, '\n\r')

            if not os.listdir(self.DIR_NAME):
                repo = git.Repo.init(self.DIR_NAME)
                origin = repo.create_remote('origin', self.REMOTE_URL)
                origin.fetch()
                origin.pull(origin.refs[0].remote_head)
            print("repo cloned successfully")
            print()
        except Exception as e:
            print(str(e))

    def git_branch(self):
        try:
            repo = git.Repo(self.DIR_NAME)
            if self.NEW_BRANCH not in repo.heads:
                repo.git.branch(self.NEW_BRANCH)
                print('branch "' + self.NEW_BRANCH + '" created successfully')
            else:
                print('branch "' + self.NEW_BRANCH + '" is already exist')
            print("available branches:")
            print(repo.heads)
            print()
        except Exception as e:
            print(str(e))

    def git_checkout(self):
        try:
            repo = git.Repo(self.DIR_NAME)
            repo.git.checkout(self.NEW_BRANCH)
            branch = repo.active_branch
            print("active branch is: " + branch.name)
        except Exception as e:
            print(str(e))


    def git_commit(self):
        try:
            repo = git.Repo(self.DIR_NAME)
            commit_message = 'work in progress'
            repo.git.add('--all')
            repo.index.commit(commit_message)
        except Exception as e:
            print(str(e))

    def git_push(self):
        try:
            repo = git.Repo(self.DIR_NAME)
            origin = repo.remote('origin')
            branch = repo.active_branch
            origin.push(branch.name)
            repo.git.add(update=True)
            print("repo push successfully")
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    a = git_operations(NAME, URL, BRANCH)
    a.git_clone()
    a.git_branch()
    a.git_checkout()
    a.git_commit()
    a.git_push()