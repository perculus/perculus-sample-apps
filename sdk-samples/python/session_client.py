import os

from perculus_sdk.client import APIClient

def print_access_token(client):
    print("--------client.access_token--------")
    print(client.access_token)
    print("-----------------------------------")

def list_sessions(client):
    sessions = client.sessions.list_sessions()
    print("--------Session List--------")
    print(sessions)
    print("-----------------------------------")

def get_session(client, session_id):
    session = client.sessions.get_session(session_id)
    print("--------Session Show--------")
    print(session)
    print("-----------------------------------")

def create_session(client, name):
    created_session = client.sessions.create_session({
        "name": name,
        "start_date": "2024-09-25T14:00:25.699Z",
        "duration": 10,
        "lang": "tr-TR",
        "options": {
            "allow_users_stream_self_cam_mic": True,
            "enable_attendance_check": False
        }
    })
    print("--------created_session--------")
    print(created_session)
    print("-----------------------------------")

def search_session(client):
    searched_session = client.sessions.search_session({
        "name": "test test",
        "description": "test"
    })
    print("--------searched_session--------")
    print(searched_session)
    print("-----------------------------------")

def update_session(client, session_id):
    updated_session = client.sessions.update_session(session_id,{
        "name": "test 123",
        "start_date": "2026-05-15T15:28:25.699Z",
        "duration": 55
        }
    )
    print("--------updated_session--------")
    print(updated_session)
    print("-----------------------------------")

def delete_session(client, session_id):
    deleted_session = client.sessions.delete_by_session_id(session_id)
    print("--------deleted_session--------")
    print(deleted_session)
    print("-----------------------------------")


if __name__ == "__main__":
    
    # API client
    client = APIClient()

    # Set your domain
    client.set_domain("<DOMAIN>")
    
    # Set your credentials
    print(client.set_credentials(
        access_key="<ACCESS_KEY>",
        secret_key="<SECRET_KEY>",
        account_id="<ACCOUNT_ID>"
    ))
    
    print_access_token(client)

    while True:
        print("\nSelect an option for session actions:")
        print("1. List Sessions")
        print("2. Get Session")
        print("3. Create Session")
        print("4. Search Session")
        print("5. Update Session")
        print("6. Delete by Session ID")
        print("7. Exit")
        
        selection = input("Enter your selection (1/2/3/4/5/6/7): ")
        
        if selection == "1":
            list_sessions(client)
        elif selection == "2":
            session_id = input("Enter Session ID: ")
            get_session(client, session_id)
        elif selection == "3":
            session_name = input("Enter Session Name: ")
            create_session(client, session_name)
        elif selection == "4":
            search_session(client)
        elif selection == "5":
            session_id = input("Enter Session ID: ")
            update_session(client, session_id)
        elif selection == "6":
            session_id = input("Enter Session ID to Delete: ")
            delete_session(client, session_id)
        elif selection == "7":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please select again.")