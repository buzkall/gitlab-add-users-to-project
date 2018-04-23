# Gitlab helper: add users to a project

This script was created to make easier the process of creating new users in your gitlab and add them as members of a project.

It's done with python 3 and uses the python-gitlab library.

The idea is to use a CSV file with the emails, names and usernames of the users and specify the project to add them to.


<p align="center">
    <img src="https://i.imgur.com/iDJuOA5.png" alt="gitlab_script_schema">
</p>



## Installation

If this case I have my local installation of python 3 with the alias python3, if you only have python 3 installed, 
you can use "python" and "pip" instead of the alias I use here.

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Modify the config file before moving it to the home folder
```bash
vi python-gitlab.example.cfg
```

This file allows you to specify the config for several gitlab installations, if you only have one, 
change the name "yourProjectName" and set it as default in line 2.
In the case of having several, the gitlab id should be specified in the script when opening
the config file (also when receiving the error: 
"gitlab.config.GitlabIDError: Impossible to get the gitlab id (not specified in config file)")
```
gl = gitlab.Gitlab.from_config('projectName', '/PATH_TO/.python-gitlab.cfg')
```

Specify your gitlab installation url in the config file and go to your Profile settings to get your access token. 
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
mv python-gitlab.example.cfg ~/.python-gitlab.cfg
```

## Usage

To use the script two parameters are needed: 
* The csv file
* the id/path of the gitlab project

The script expects to find this three columns in the csv (with this order and with a header row like in the example file):
* email
* username
* name


```python
python3 add_users_to_project.py YOUR_FILE.csv USER/PROJECT-NAME
```

#### Output
```
Created user with email: test1@mail.com - id: 51
Added user user with email: test1@mail.com to the project
Created user with email: test2@mail.com - id: 52
Added user user with email: test2@mail.com to the project

```


If one of the user was already created or was already a member, it will skip the process.

```python¬
User already exists with email: test1@mail.com - id: 51
User user with email: test1@mail.com already a member of the project
User already exists with email: test2@mail.com - id: 52
User user with email: test2@mail.com already a member of the project
```


<p align="center">
    <img src="https://i.imgur.com/w7V6D55.png" alt="iterm_capture">
</p>

