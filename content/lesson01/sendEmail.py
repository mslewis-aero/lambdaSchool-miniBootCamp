import requests

message = 'Testing out posting to a form via Python.\n'
message = message + 'Thanks so much for doing this class!\n'
message = message + 'How would we know to post to /contact-form instead of /contact?'


myData = {
    'name':'Michael',
    'lastname':'Lewis',
    'email':'mslewis.aero@gmail.com',
    'message':'Testing out posting to a form. \n Thanks so much for doing this class!'
}

r = requests.post('https://lambdaschool.com/contact-form', json = myData)

print('Status: ' + str(r.status_code) + '\nwhich means: ' + r.reason)

print('Text Response:\n' + r.text)
