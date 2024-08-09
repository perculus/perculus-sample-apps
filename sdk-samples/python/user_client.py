import os

from perculus_sdk_python.client import APIClient


def print_access_token(client):
    print("--------client.access_token--------")
    print(client.access_token)
    print("-----------------------------------")

def create_user(client, user):
    user = client.users.create_user(user)
    print("--------user create --------")
    print(user)
    print("-----------------------------------")

def update_user(client, user_id):
    user = client.users.update_user(user_id,{
        "name": "test username1"
    })
    print("--------user update --------")
    print(user)
    print("-----------------------------------")

def delete_by_user_id(client, user_id):
    user = client.users.delete_by_user_id(user_id)
    print("--------delete_by_user_id --------")
    print(user)
    print("-----------------------------------")

def search_user(client, name):
    #user_id, name, surname, username, email, role, mobile, page_size, page_number
    search_user = client.users.search_user({
        "name": name
    })
    print("--------search_user --------")
    print(search_user)
    print("-----------------------------------")

def get_user_by_id(client, user_id):
    getuserbyid = client.users.get_user_by_id(user_id)
    print("--------getuserbyid --------")
    print(getuserbyid)
    print("-----------------------------------")

def get_user_by_username(client, username):
    getuserbyusername = client.users.get_user_by_username(username)
    print("--------getuserbyusername --------")
    print(getuserbyusername)
    print("-----------------------------------")


if __name__ == "__main__":

    # API client
    client = APIClient()

    # Set your domain
    client.set_domain("<DOMAIN>")
    
    # Set your credentials
    client.set_credentials(
        access_key="<ACCESS_KEY>",
        secret_key="<SECRET_KEY>",
        account_id="<ACCOUNT_ID>"
    )
    
    print_access_token(client)

    while True:
        print("\nSelect an option for session actions:")
        print("1. Create User")
        print("2. Update User")
        print("3. Delete by User ID")
        print("4. Search User")
        print("5. Get User By ID")
        print("6. Get User By UserName")
        print("7. Exit")
        
        selection = input("Enter your selection (1/2/3/4/5/6/7): ")
        
        if selection == "1":
            user_first_name = input("Enter User First Name: ")
            user_surname = input("Enter User Surname: ")
            user_username = input("Enter UserName: ")
            user_email = input("Enter User Email: ")
            create_user(client, {
                "name": user_first_name,
                "surname": user_username,
                "username": user_username,
                "email": user_email
            })
        elif selection == "2":
            user_id = input("Enter User ID: ")
            update_user(client, user_id)
        elif selection == "3":
            user_id = input("Enter User ID: ")
            delete_by_user_id(client, user_id)
        elif selection == "4":
            user_name = input("Enter User Name: ")
            search_user(client, user_name)
        elif selection == "5":
            user_id = input("Enter User ID: ")
            get_user_by_id(client, user_id)
        elif selection == "6":
            username = input("Enter UserName: ")
            get_user_by_username(client, username)
        elif selection == "7":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please select again.")