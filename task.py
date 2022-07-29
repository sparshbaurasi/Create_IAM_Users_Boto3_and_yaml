import yaml
import boto3
client = boto3.client('iam')
from yaml.loader import SafeLoader

# creating a user creating function 

def func_create_user(userName):
    try:
       response = client.create_user(UserName=userName)
       return response
    except Exception as e:
      if userName == 'SuperAdmin':
        print('error')

# assigning groups to users

def func_group_assignment(grpName,usrName):
    try:
       response = client.add_user_to_group(GroupName=grpName,UserName=usrName)
    except Exception as e:
      if usrName == 'SuperAdmin' and grpName == 'SuperAdmin':
        print('error')

# Open the file and load the file
with open('users.yaml') as f:
    documents = yaml.load(f, Loader=SafeLoader)

for key in documents['Users']:
    func_create_user(key)
for i in documents['GroupAssignment']:
    tup1=(documents['GroupAssignment'].get(i))
    for j in tup1:
     func_group_assignment(i,j)
      
    
        # data["GroupAssignment"][group]