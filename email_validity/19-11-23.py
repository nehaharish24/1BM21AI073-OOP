#program to check the validity of a mail id

def is_valid_email(email):
    if len(email)<=256:
        if '@' in email:
            at_position = email.index('@')
            if at_position > 0:
                if '.' in email:
                    dot_index=email.index('.')
                    if 0 < at_position < len(email) - 1 and at_position < dot_index < len(email) - 1:
                        if dot_index != -1 and dot_index < len(email) - 1:
                            if email[0].isalpha() or email[0].isdigit():
                                return True
    else:
        return False
    
print("Enter the email address")
email_id=input()
res=is_valid_email(email_id)
if res:
    print("Valid email")
else:
    print("Invalid email")
