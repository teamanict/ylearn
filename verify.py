import requests, json
key = 'FLWSECK_TEST-0381a6db2cb5e7656a65cf0b6d95a8b1-X'

def verify_trans(id):
    #send request to https://api.flutterwave.com/v3/transactions/:id/verify
    string = f'https://api.flutterwave.com/v3/transactions/{id}/verify'
 
    response = requests.get(string, headers={'Authorization': 'Bearer ' + key})
    transaction = json.loads(response.text)
    print(id, string, response.json())

    #Verify transaction data
    if transaction['data']['status'] == 'successful' and transaction['data']['amount'] >= 15000 and transaction['data']['meta']['__CheckoutInitAddress'] == 'http://127.0.0.1:5000/pay':
        return 'YEYY!!! Success'
    else:
        return f'Error while verifying transaction. </br> Please contact support immediately with this id: </br>{id}</br>'
 


