import csv
import argparse
from random import randint
from typing import List, Dict

fieldnames = [
    "name",
    "password",
    "tags",
    "expires",
    "notes",
]  # <- subject to change as 4CAT updates


def bulk_user_creator(
    groups: int,
    name: str,
    password: str,
    tag: str,
    expiration: str = None,
    notes: str = None,
) -> List[Dict]:
    """
    Function to bulk create X amount of usernames for each NavCom group. name, password and tag are required, other arguments are optional.
    It's used to populate a list with users with a similar base name and an unhashed  password.
    Args:
        groups (int) -> the number of student groups for NavCom
        name (str)-> base name for what will become the group's username
        password (str)-> password for user
        expiration (str)-> OPTIONAL, expiry date for user
        tags (str or list of strings)-> tag assigned to user. Used by 4CAT for user management
        notes -> OPTIONAL, any notes for this bulk user/groups creation.

    Example of output list:
        [{name: basename_1, password: pass_4, expiration: None, tags: None, notes: None},
        {name: basename_2, password: pass_4, expiration: None, tags: None, notes: None}]
    """

    data = []

    for i in range(1, groups + 1):
        user_data = {
            fieldnames[0]: f"{name}_g{str(i)}",
            fieldnames[1]: f"{password}_{str(randint(0,2024))}",
            fieldnames[2]: tag,
            fieldnames[3]: expiration,
            fieldnames[4]: notes,
        }
        data.append(user_data)

    return data


def csv_maker(data: List[Dict], filename: str) -> None:
    """
    Function to create a CSV file for bulk user creation

    Args:
        data (list of dictionaries) -> data about the users to be written into the csv
        filename (str) -> name of the output csv file

    """
    if not filename.endswith(".csv"):
        filename += ".csv"

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in data:
            if all(
                key in user for key in fieldnames
            ):  # Ensure all required keys are present
                writer.writerow(user)


def main() -> None:
    """
    Main function that lets the tool be run as a CLI tool
    """
    print("Starting script...")
    parser = argparse.ArgumentParser(
        description="Creates a CSV file with bulk user data."
    )
    parser.add_argument("groups", type=int, help="Number of student groups")
    parser.add_argument("name", type=str, help="Base name for the group's username")
    parser.add_argument("password", type=str, default=None, help="Password for user")
    parser.add_argument("tag", type=str, default=None, help="Tags assigned to user")
    parser.add_argument(
        "--expiration", type=str, default=None, help="Expiry date for user"
    )
    parser.add_argument(
        "--notes", type=str, default=None, help="Notes for this bulk user creation"
    )
    parser.add_argument("output_file", type=str, help="Name of the output CSV file")

    args = parser.parse_args()

    user_data = bulk_user_creator(
        args.groups, args.name, args.password, args.tag, args.expiration, args.notes
    )
    csv_maker(user_data, args.output_file)


if __name__ == "__main__":
    main()
    print("All done, file created")
