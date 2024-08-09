import os

from perculus_sdk_python.client import APIClient

def print_access_token(client):
    print("--------client.access_token--------")
    print(client.access_token)
    print("-----------------------------------")

def add_by_user_id(client, session_id, user_id):
    add_by_user_id = client.attendees.add_by_user_id(session_id, user_id)
    print("--------add_by_user_id--------")
    print(add_by_user_id)
    print("-----------------------------------")

def add_multiple_by_user_id(client, session_id):
    # role Default is "u". Possible values: e a u e+
    add_multiple_by_user_id = client.attendees.add_multiple_by_user_id(session_id, [{
        "user_id": "<USER_ID>",
        "role": "u"
    },{
        "user_id": "<USER_ID>",
        "role": "u"
    }])
    print("--------add_multiple_by_user_id--------")
    print(add_multiple_by_user_id)
    print("-----------------------------------")

def update_by_attendance_code(client):
    update_by_attendance_code = client.attendees.update_by_attendance_code(
        session_id="<SESSION_ID>",
        attendance_code="<ATTENDANCE_CODE>",
        attendee={
        "user_id": "<USER_ID>",
        "role": "e"
    })
    print("--------update_by_attendance_code--------")
    print(update_by_attendance_code)
    print("-----------------------------------")

def update_by_email(client):
    update_by_email = client.attendees.update_by_email(
        session_id="<SESSION_ID>",
        email="<EMAIL>",
        attendee={
        "user_id": "<USER_ID>",
        "role": "u"
    })
    print("--------update_by_email--------")
    print(update_by_email)
    print("-----------------------------------")


def get_by_attendance_code(client):
    get_by_attendance_code = client.attendees.get_by_attendance_code(
        session_id="<SESSION_ID>",
        attendance_code="<ATTENDANCE_CODE>"
    )
    print("--------get_by_attendance_code--------")
    print(get_by_attendance_code)
    print("-----------------------------------")
    

def search_attendees(client):
    #user_id, attendance_code, name, surname, email,role,mobile,page_size, page_number
    search_attendees = client.attendees.search_attendees(
        session_id="<SESSION_ID>",
        params={
            "name": "test name",
            "role": "u"
        }
    )
    print("--------search_attendees--------")
    print(search_attendees)
    print("-----------------------------------")

def get_by_email(client):
    get_by_email = client.attendees.get_by_email(
        session_id= "<SESSION_ID>",
        email="<EMAIL>"
    )
    print("--------get_by_email--------")
    print(get_by_email)
    print("-----------------------------------")

def delete_by_attendance_code_or_user_id(client):
    delete_by_attendance_code_or_user_id = client.attendees.delete_by_attendance_code_or_user_id(
        session_id="<SESSION_ID>",
        attendance_code_or_user_id="<ATTENDANCE_CODE_OR_USER_ID>"
    )
    print("--------delete_by_attendance_code_or_user_id--------")
    print(delete_by_attendance_code_or_user_id)
    print("-----------------------------------")

def delete_by_email(client):
    delete_by_email = client.attendees.delete_by_email(
        session_id="<SESSION_ID>",
        email="<EMAIL>"
    )
    print("--------delete_by_email--------")
    print(delete_by_email)
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
        print("1. Add by User ID")
        print("2. Add Multiple by User ID")
        print("3. Update by Attendance Code")
        print("4. Update by Email")
        print("5. Get by Attendance Code")
        print("6. Search Attendees")
        print("7. Get Attendee by Email")
        print("8. Delete by Attendance Code or User ID")
        print("9. Delete by Email")
        print("10. Exit")
        
        selection = input("Enter your selection (1/2/3/4/5/6/7/8/9/10): ")
        
        if selection == "1":
            session_id = input("Enter Session ID: ")
            user_id = input("Enter User ID: ")
            add_by_user_id(client, session_id, user_id)
        elif selection == "2":
            session_id = input("Enter Session ID: ")
            add_multiple_by_user_id(client, session_id)
        elif selection == "3":
            update_by_attendance_code(client)
        elif selection == "4":
            update_by_email(client)
        elif selection == "5":
            get_by_attendance_code(client)
        elif selection == "6":
            search_attendees(client)
        elif selection == "7":
            get_by_email(client)
        elif selection == "8":
            delete_by_attendance_code_or_user_id(client)
        elif selection == "9":
            delete_by_email(client)
        elif selection == "10":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please select again.")