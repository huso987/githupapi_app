
import re
import requests
import json 
from github import Github



class Ghub:
   def __init__(self):
      self.url="https://api.github.com"
      self.token="****pushtoken*****"
      
      
   def getUser(self,uname):   
      cevap=requests.get(self.url+"/users/"+uname)
      return cevap.json()
   def getRepo(self,uname):
      cevap=requests.get(self.url+"/users/"+uname+"/repos")
      return cevap.json()
   def createRepo(self,name):
      login=Github(self.token)
      user=login.get_user()
      new_repo = user.create_repo(name)
      new_repo.create_file("New-File.txt", "new commit", "Data Inside the File")
      print("Repository Created".center(50,"*"))
   def deleteRepo(self,name):
      login=Github(self.token)
      user=login.get_user()
      repo=user.get_repo(name)
      repo.delete()
      print("Repository Deleted".center(50,"*"))
   def make_github_issue(self,reponame,iname):
      login=Github(self.token)
      user=login.get_user()
      repo=user.get_repo(reponame)
      issue=repo.create_issue(iname)
      issue.create_comment("huseyin doğdu")
      print("Issue Created".center(50,"*"))
   def close__github_issue(self,username,Repositoryname,isno):
      headers = {"Authorization" : "token {}".format(self.token)}
      data = {"state": "close"}
      url = "https://api.github.com/repos/{}/{}/issues/{}".format(username,Repositoryname,isno)
      requests.post(url,data=json.dumps(data),headers=headers)
      print("Issue closed".center(50,"*"))
   def make_open_issue(self,username,Repositoryname,isno):
      headers = {"Authorization" : "token {}".format(self.token)}
      data = {"state": "open"}
      url = "https://api.github.com/repos/{}/{}/issues/{}".format(username,Repositoryname,isno)
      requests.post(url,data=json.dumps(data),headers=headers)
      print("Issue opened".center(50,"*"))
   
     
     
      

git=Ghub()

while True:
   choice=input("1-Find user\n2-Get Repositories\n3-Create Repository\n4-Delete Repository\n5-Issue\n6-Close Issue\n7-Reopen Issue\n8-Exit\nSeçiminiz=")
   if choice=="1":
      uname=input("username=")
      rest=git.getUser(uname)
      print("User".center(50,"*"))
      print(f'name: {rest["name"]} \ncreated_at:{rest["created_at"]} \nurl:{rest["url"]}')
      print("".center(50,"*"))
   elif choice=="2":
      uname=input("username=")
      rest=git.getRepo(uname)
      print("Repositories".center(50,"*"))
      for i in rest:
         print(i["name"]+"--"+i["created_at"])
      print("".center(50,"*"))
   elif choice=="3":
      reponame=input("reponame=")
      rest=git.createRepo(reponame)     
   elif choice =="4":
      reponame=input("reponame=")
      rest=git.deleteRepo(reponame)
   elif choice=="5":
      issuename = input("Enter issue: ")
      Repositoryname = input("Enter repository name: ")
      rest=git.make_github_issue(Repositoryname,issuename)
   elif choice=="6":
      username = input("Enter Github username: ")
      Repositoryname = input("Enter repository name: ")
      isno=input("isssuno:")
      rest=git.close__github_issue(username,Repositoryname,isno)
   elif choice=="7":
      username = input("Enter Github username: ")
      Repositoryname = input("Enter repository name: ")
      isno=input("isssuno:")
      rest=git.make_open_issue(username,Repositoryname,isno)
   elif choice=="8":
      break
   else:
      print("Hatali giriş!!!")