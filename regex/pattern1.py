import re

text = "Jun 05 14:32:01 server01 sshd[12345]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50  user=root"
pattern = r"authentication"

match = re.search(pattern, text)

if match:
    print(f"Match found: {match.group()}")
else:
    print(f"Match not found")