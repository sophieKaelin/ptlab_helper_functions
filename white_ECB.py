import urllib.parse, base64

token = str(input("Enter the BASE64 Encoded ECB cookie: "))
print("\n\n\t*** NEW Cookie IS: ***\n\n")

token = bytearray(base64.b64decode(urllib.parse.unquote(token))) # Decode cookie and convert to array of bytes
del token[0:8] # Assuming a username was created with first 8 bytes random, and next 5 "admin", delete random bytes
token = urllib.parse.quote(base64.b64encode(bytes(token))) # Encode value to create admin cookie 
print (token)
