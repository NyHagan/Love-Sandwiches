import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    get sales data from user
    """
    print("Please enter sales data into the space provided")
    print("be sure to use exactly six numbers separated by a comma\n")

    data_str = input("Enter your data here")
       
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    converts strings into integers and throws error if not able to. also ensures there are only 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"expected exactly 6 values,you entered {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data:{e}, please try again.\n")


get_sales_data()  