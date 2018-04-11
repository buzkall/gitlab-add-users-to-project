#!/usr/bin/env python3
import gitlab
import sys
import urllib.parse
import csv

if len(sys.argv) != 3:
    print("Please provide a CSV file and a project.")
    sys.exit(1)

file = sys.argv[1]
project = sys.argv[2]

gl = gitlab.Gitlab.from_config()

# verify the project exists
# first convert the / to url encode
project_encoded = urllib.parse.quote_plus(project)

try:
    project = gl.projects.get(project_encoded)

except gitlab.GitlabGetError:
    print("No project with that id")

# get all existing users
users = gl.users.list(all=True)

with open(file, newline='') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    header = next(data)

    for row in data:
        email = row[0]
        username = row[1]
        name = row[2]

        # check if user already exists
        user_id = None
        for user in users:
            if user.email == email:
                user_id = user.id

        if user_id is None:
            new_user = gl.users.create({'email': email,
                                        'reset_password': 'yes',
                                        'username': username,
                                        'name': name})
            user_id = new_user.id
            print('Created user with email: ' + email + " - id: " + str(new_user.id))
        else:
            print('User already exists with email: ' + email + " - id: " + str(user_id))

        # Add the user to the project
        existing_members = project.members.list(all=True)
        user_is_already_member = False
        for member in existing_members:
            if member.id == user_id:
                user_is_already_member = True
                print("User user with email: " + email + " already a member of the project")

        if not user_is_already_member:
            member = project.members.create({'user_id': user_id, 'access_level': gitlab.Group.DEVELOPER_ACCESS})
            print("Added user user with email: " + email + " to the project")
