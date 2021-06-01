import uuid
import recurly
import names

api_key = 'api_key'
client = recurly.Client(api_key)


accountList = client.list_accounts().items()
newID = uuid.uuid4()
for x in accountList:
    while(newID == x.code):
        newID = uuid.uuid4()
strId = str(newID)
    
#CREATE ACCOUNT WITH BILLING INFO

fname = str(names.get_first_name(gender=None))
lname = str(names.get_last_name())

print(f'{fname} {lname} owns account {newID}')

try:
    account_create = {
        "first_name":fname,
        "last_name":lname,
        "code": strId,
        "shipping_addresses": [
            {
                "nickname": "Home",
                "street1": "1 Tchoupitoulas St",
                "city": "New Orleans",
                "region": "LA",
                "country": "US",
                "postal_code": "70115",
                "first_name": fname,
                "last_name": lname
            }
        ],
        "billing_info":
            {"first_name": fname,
            "last_name": lname,
            "address": {
                "phone" : "7188349909",
                "street1":"123 Main",
                "city":"Brooklyn",
                "region":"New York",
                "postal_code": "11220",
                "country": "US",
                },
        "transaction_type": "moto",
        "account_type":"checking",
        "name_on_account": "BANK OF RECURLY",
        "account_number": "11111111",
        "routing_number": "123456780"} 
        }
    account = client.create_account(account_create)
    print("Created Account %s" % account)
except recurly.errors.ValidationError as e:
    # If the request was invalid, you may want to tell your user
    # why. You can find the invalid params and reasons in e.error.params
    print("ValidationError: %s" % e.error.message)
    print(e.error.params)
except recurly.ApiError as e:
    print(f'ApiError {e.error}')
