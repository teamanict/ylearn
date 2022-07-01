import requests, json, datetime
import resources.modules.database as db
flutterwave_key = 'FLWSECK_TEST-0381a6db2cb5e7656a65cf0b6d95a8b1-X'

def verify_trans(id):
    #send request to https://api.flutterwave.com/v3/transactions/:id/verify
    string = f'https://api.flutterwave.com/v3/transactions/{id}/verify'
 
    response = requests.get(string, headers={'Authorization': 'Bearer ' + flutterwave_key})
    transaction = json.loads(response.text)

    #Verify transaction data
    amount=transaction['data']['amount']; child_id=transaction['data']['meta']['child_id'];
    if transaction['data']['status'] == 'successful' and amount >= 15000 and transaction['data']['meta']['__CheckoutInitAddress'] == 'http://127.0.0.1:5000/pay':
        return addPayment(child_id, amount);
    else:
        return f'Error while verifying transaction. </br> Please contact support immediately with this id: </br>{id}</br> 1'
 
def addPayment(child_id, amount):
    #Insert current date into mysql children lastpayment column
    db.runDBQuery(db.users_db,f'UPDATE children SET lastpayment = CURRENT_DATE WHERE username = "{child_id}";')
    return f'Payment successful. </br> Thank you for your payment of UGX{amount}'
    #else: return f'Error while adding payment. </br> Please contact support immediately with this id: </br>{child_id} 2</br>'

def isSubscribed(child_id):
    #Get date of subscription from mysql children Lastpayment column
    lastpayment = db.runDBQuery(db.users_db,f'SELECT LastPayment FROM children WHERE username="{child_id}";')

    #Convert date to datetime object
    lastpayment = lastpayment['LastPayment']
    lastpayment = datetime.datetime.strptime(lastpayment, '%Y-%m-%d')

    if lastpayment is None:
        #No payment made yet
        return False
    else:
    #Find if 30 days has passed since last payment
        if(datetime.datetime.now() - lastpayment).days > 30:
            #Month has passed, no subscription
            return False
        else:
            #Month has not passed, subscription is active
            return True




