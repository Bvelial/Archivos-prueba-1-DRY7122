import json

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

token = ourjson.get("access_token")
expiresIn = ourjson.get("expires_in")

if expiresIn > 0:
    print("El token de acceso es : ", token)
    print("El token expira en: ", expiresIn," segundos.")
