
# What are dictionaries?
# key-value pairs, retrieved by either its key, or its value.
# syntax: {}
# lists can exist within the dictionary

dev= {
        "key": "value",
        "name": "James",
        "stream": "DevOps",
        "completed": 3,
        "completed_names": ['Variables', 'Data Types', 'Collections']

        }

print(dev)
# confirm the type is dictionary
print(type(dev))

# Getting values from dictionaries
print(dev['name'])

print(dev['completed_names'][1])


# TASK
# Add 'operators' as value of completed lesson names
dev['completed_names'].append('Operators')

# Change completed number to 4
dev['completed'] = 4

# Remove 'Data Type' from completed lesson names
dev['completed_names'].remove('Data Types')


# What are sets?
# syntax: {}
# they are mutable
# their ordering does not matter (notice how they change order occasionally when the script is run)

car_parts = {"wheels", "windows", "doors"}
print(type(car_parts))
print(car_parts)

# Adding to sets
car_parts.add('seats')
# Removing from sets
car_parts.discard('doors')

print(car_parts)
