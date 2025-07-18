import pandas as pd
import os

def create_csv_file(file_path):
    data = [
        {"Title": "Today's Money", "Value": 53000, "Change": 55, "ChangeType": "positive", "Prefix": "$"},
        {"Title": "Today's Users", "Value": 2300, "Change": 5, "ChangeType": "positive", "Prefix": ""},
        {"Title": "Ads Views", "Value": 3462, "Change": -5, "ChangeType": "negative", "Prefix": ""},
        {"Title": "Sales", "Value": 103430, "Change": -5, "ChangeType": "negative", "Prefix": "$"}
    ]
    
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ File CSV created at: {file_path}")


def create_csv_Website_Views_File(file_path):
    data = {
        'Day': ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        'Views': [50, 45, 22, 28, 50, 60, 76]
    }
    
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ File Website Views CSV created at: {file_path}")

def create_csv_daily_sales(file_path):
    """
    Tạo file CSV cho dữ liệu Daily Sales
    Cấu trúc: Month, Sales
    """
    data = {
        'Month': ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
        'Sales': [120, 230, 130, 440, 250, 360, 270, 180, 90, 300, 310, 220]
    }
    
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ File Daily Sales CSV created at: {file_path}")

def create_csv_completed_tasks(file_path):
    data = {
        'Month': ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Tasks': [50, 40, 300, 220, 500, 250, 400, 230, 500]
    }
    
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ File Completed Tasks CSV created at: {file_path}")


def create_projects_csv(file_path):
    projects = [
        {
            "ProjectName": "Material XD Version",
            "Members": ["R", "H", "A", "J"],
            "Budget": 14000,
            "Progress": 60,
            "ProgressPercent": "60%"
        },
        {
            "ProjectName": "Add Progress Track",
            "Members": ["H", "J"],
            "Budget": 3000,
            "Progress": 10,
            "ProgressPercent": "10%"
        },
        {
            "ProjectName": "Fix Platform Errors",
            "Members": ["A", "R"],
            "Budget": "Not set",
            "Progress": 100,
            "ProgressPercent": "100%"
        },
        {
            "ProjectName": "Launch our Mobile App",
            "Members": ["J", "A", "J", "R"],
            "Budget": 20500,
            "Progress": 100,
            "ProgressPercent": "100%"
        },
        {
            "ProjectName": "Add the New Pricing Page",
            "Members": ["M"],
            "Budget": 500,
            "Progress": 25,
            "ProgressPercent": "25%"
        },
        {
            "ProjectName": "Redesign New Online Shop",
            "Members": ["H", "J"],
            "Budget": 2000,
            "Progress": 40,
            "ProgressPercent": "40%"
        }
    ]
    
  
    data = {
        "ProjectName": [],
        "Members": [],
        "Budget": [],
        "Progress": [],
        "ProgressPercent": []
    }
    
    for project in projects:
        data["ProjectName"].append(project["ProjectName"])
        data["Members"].append(",".join(project["Members"]))
        data["Budget"].append(project["Budget"])
        data["Progress"].append(project["Progress"])
        data["ProgressPercent"].append(project["ProgressPercent"])
    
    df = pd.DataFrame(data)
    
   
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
  
    df.to_csv(file_path, index=False)
    print(f"✅ File projects CSV created at: {file_path}")

def create_orders_csv(file_path):
    """
    Tạo file CSV cho dữ liệu Orders Overview
    Cấu trúc: ID, IconClass, Icon, Title, Description, Date
    """
    orders = [
        {
            "IconClass": "bg-success",
            "Icon": "fa-bell",
            "Title": "$2400, Design changes",
            "Description": "Design changes request",
            "Date": "22 DEC 7:20 PM"
        },
        {
            "IconClass": "bg-danger",
            "Icon": "fa-code",
            "Title": "New order #1832412",
            "Description": "New order received",
            "Date": "21 DEC 11 PM"
        },
        {
            "IconClass": "bg-info",
            "Icon": "fa-shopping-cart",
            "Title": "Server payments for April",
            "Description": "Monthly server payment",
            "Date": "21 DEC 9:34 PM"
        },
        {
            "IconClass": "bg-warning",
            "Icon": "fa-credit-card",
            "Title": "New card added for order #4395133",
            "Description": "Payment method updated",
            "Date": "20 DEC 2:20 AM"
        },
        {
            "IconClass": "bg-primary",
            "Icon": "fa-unlock",
            "Title": "Unlock packages for development",
            "Description": "Development access granted",
            "Date": "18 DEC 4:54 AM"
        },
        {
            "IconClass": "bg-success",
            "Icon": "fa-shopping-bag",
            "Title": "New order #8583120",
            "Description": "New customer order",
            "Date": "17 DEC"
        }
    ]
    

    for idx, order in enumerate(orders, start=1):
        order['ID'] = idx
    
    df = pd.DataFrame(orders)
    

    df = df[['ID', 'IconClass', 'Icon', 'Title', 'Description', 'Date']]
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ File orders CSV created at: {file_path}")
if __name__ == "__main__":
    create_csv_file("./data/firstdata.csv")
    create_csv_Website_Views_File("./data/website_views.csv")
    create_csv_daily_sales("./data/daily_sales.csv")
    create_csv_completed_tasks("./data/completed_tasks.csv")
    create_projects_csv("./data/projects.csv")
    create_orders_csv("./data/orders.csv") 