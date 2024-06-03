#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the script receives an argument
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    # Get the employee ID from the argument
    employee_id = int(sys.argv[1])
    
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch the employee details
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)
    user_data = user_response.json()
    
    # Get the employee name and username
    employee_username = user_data.get("username")
    
    # Fetch the employee's TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Define the filename
    filename = "{}.csv".format(employee_id)
    
    # Open the CSV file for writing
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        # Write the data to the CSV file
        for task in todos_data:
            csv_writer.writerow([
                employee_id,
                employee_username,
                task.get("completed"),
                task.get("title")
            ])
    
    print("Data exported to {}".format(filename))
