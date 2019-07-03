dup_email_file = "emails.txt"

dups_removed_email_file = "duplicate-free-email-list.txt"

with open(dup_email_file) as file_object:
    emails = file_object.read().replace('\n', '').split(', ')

dups_removed = []

def remove_duplicate_emails(array):
    for email in emails:
        if email not in dups_removed:
            dups_removed.append(email)
    return dups_removed

dups_array = remove_duplicate_emails(emails)


with open(dups_removed_email_file, 'w') as f:
    email_txt = ', '.join(dups_array)
    f.write(email_txt)

print("\nDONE")