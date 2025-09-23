def get_full_name(first_name, last_name, middle_name=None):
    print(f"{first_name} {middle_name or ''} {last_name}")
get_full_name("John", "lee") # Way number 1
get_full_name(first_name="john", middle_name="hooker", last_name="lee") # Way number 2
