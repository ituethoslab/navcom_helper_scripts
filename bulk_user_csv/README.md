# Bulk user creation using CSV and 4CAT import functionality

This CLI application creates a CSV file that can be imported into 4CAT for bulk user creation.

It takes in the following arguments

## Example of usage

The function requires the following arguments:

**groups**: The number of groups in the NavCom cohort
**name**: Base name for the student groups, for example 'navcom24'
**password**: Base password for the user, a random number will be appended to this
**tag**: A tag for later bulk dataset management, usually the same as the cohort name _i.e_ 'navcom24'
**output_file**: The desired name for the CSV file

Two more arguments exist, but these are optional:

**expiration**: Sets an expiration date for the users being created
**notes**: Adds a note for this bulk user creation

### Example of usage in the terminal

The following command:
`python user_csv_creator.py 28 navcom24 sofa navcom24 navcom24_groups.csv`

Will output a CSV file called `navcom24_groups.csv` with content like this: 

`
name,password,tags,expires,notes
navcom24_g1,sofa_1833,navcom24,,
navcom24_g2,sofa_480,navcom24,,
navcom24_g3,sofa_1916,navcom24,,
navcom24_g4,sofa_1059,navcom24,,
`
## Importing to 4CAT

To import to 4CAT follow this steps while logged in as admin:
1. Go into 'Contro Panel' -> 'Users'
2. Click on 'Create users (bulk)' on the right
3. Browse for the created CSV file and click on "Upload and create users"
4. Done
