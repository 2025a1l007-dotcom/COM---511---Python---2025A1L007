@Take an email address and print username ,domain and reversed domain.
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
reverse_domain = domain[::-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reverse_domain)