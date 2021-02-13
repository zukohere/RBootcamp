# Dictionary full of info
my_info = {"Name": "Matt",
            "Hobbies": ["Video Games", "Base Jumping", "Time Travel", "Baking"],
            "WakeUp": {"Sun":7, "Mon":9, "Tues":8, "Wed":10}}

# Print out results are stored in the dictionary
print(f'{my_info["Name"]}')
print(f'{my_info["Hobbies"][0] , my_info["Hobbies"][3]}')
print(f'{int(my_info["WakeUp"]["Sun"])}')