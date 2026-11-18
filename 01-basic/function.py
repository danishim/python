# Validation Function. Task: check if its email
def is_valid_email(email):
    return "@" in email and "." in email

# Action Function. Task: store application log message in a file
def write_log(message):
    with open(r"app.log", "a") as file:
        file.write(message + "\n")

# Transformer Function. Task: clean an email and split it into username and domain
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split("@")
    return {"username": username,
            "domain": domain}

# Orchestrator Function. Workflow/pipeline etc
def process_user_email(email):
    write_log("App started")
    if not is_valid_email(email):
        write_log(f"Invalid email received: {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed email: {clean_email}")
    write_log("App stopped")

# user input
email = input("please enter your email: ")
process_user_email(email)