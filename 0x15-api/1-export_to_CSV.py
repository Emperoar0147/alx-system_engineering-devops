#!/usr/bin/python3
"""Exports the to-do list information for an employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments.
    user_id = sys.argv[1]

    # Define the base URL JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API.
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
