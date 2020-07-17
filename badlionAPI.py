import json

disallowed = {
    'modsDisallowed': {
    }
}

while True:
    entry = str(input('Enter disallowed mod ([Enter] to finish): '))
    
    if entry == '':
        break
    
    disallowed['modsDisallowed'][entry] = {
            "disabled": True
        }
        
print(json.dumps(disallowed,indent=4))
input('\nPress [Enter] to close...')