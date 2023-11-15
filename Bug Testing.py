import re

my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com",
             "yourfavoriteband@g6.org", "@codingtemple.com"]

# You can also use the $ at the end of your compile expression -- this stops the search
          
#email_found = re.compile('[A-Za-z0-9-]+@[A-Za-z0-9-]+.com|org$')
#found_email = email_found.findall(email_found)
#print(found_email)

for name in my_emails:
    match = re.compile('[A-Za-z0-9-]+@[A-Za-z0-9-]+.com|[A-Za-z0-9-]+@[A-Za-z0-9-]+.org$')
    found = match.findall(name)
    if found:
        print(found)
    else:
        print("None")

