# Gitlab helper: add users to a project

This script was created to make easier the process of creating new users in your gitlab and add them as members of a project.

It's done with python 3 and uses the python-gitlab library.

The idea is to use a CSV file with the emails, names and usernames of the users and specify the project to add them to.


## Instalation

If this case I have python 3 with the alias python3, if you only have python 3 installed, you can use python and pip instead
of the ones I put here

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Modify the config file before moving it to the home folder
```bash
vi python-gitlab.cfg
```

This file allows you to specify the config for several gitlab installations, if you only have one, 
change the name "yourProjectName" and set it as default in line 2.
In the case of having several, the gitlab id should be specified in the script when opening
the config file (also when receiving the error: 
"gitlab.config.GitlabIDError: Impossible to get the gitlab id (not specified in config file)")
```
gl = gitlab.Gitlab.from_config('projectName', '/PATH_TO/.python-gitlab.cfg')
```

Specify your gitlab installation url and go to your Profile settings to get your access token. 
[Gitlab help page to get your token.](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

```python
[global]
default=yourProjectName
ssl_verify=false
true=60

[yourProjectName]
url=http:/YOUR_URL.COM
private_token=xxxxxx
api_version=4 
```

Now move the file to your home folder and add the dot before to convert it to a hidden file. 
The python-gitlab library expects this file to be there to login

```bash
mv python-gitlab.cfg ~/.python-gitlab.cfg
```

## Usage

To use the script two parameters are needed: 
* The csv file
* the id/path of the gitlab project


```python
python add_users_to_project.py import.csv root/test-api
```

#### Output
```
Created user with email: test1@mail.com - id: 51
Added user user with email: test1@mail.com to the project
Created user with email: test2@mail.com - id: 52
Added user user with email: test2@mail.com to the project

```
If one of the user was already created, it will skip the creation process.