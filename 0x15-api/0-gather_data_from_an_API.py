#!/usr/bin/python3
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
    
    # Get the employee name
    employee_name = user_data.get("name")
    
    # Fetch the employee's TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Count the total and completed tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    
    # Print the TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
