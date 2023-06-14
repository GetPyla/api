# api
Some sample files to use GetPyla API

## Python
To use this samples, don't forget to adjust parameters in config.py
```
EMAIL_SMTP_SENDER = ""      # Sender and login to your SMTP server eg: philippe@example.org
EMAIL_SMTP_RECIPIENT = ""   # Recipient for sample emails eg: philippe@example.org
EMAIL_SMTP_SERVER = ""      # SMTP server address eg: smtp.gmail.com
EMAIL_SMTP_PORT =           # SMTP server port eg: 465
EMAIL_SMTP_PASSWORD = ""    # SMTP server password 
API_SERVER = ""             # API url eg: https://api.getpyla.com
API_TOKEN = ""              # OpenID Token eg: https://id.getpyla.com/openid/token
API_CLIENT_ID = ""          # Client ID deliver by GetPyla
API_CLIENT_SECRET = ""      # Client secret delivered by GetPyla
```

### How to get created users
send_created_users.py

### How to send users that the manager did not onboard yet
send_waiting_users_to_manager.py

### Get list of users who arrive in five days
start_in_five_days.py


### Get list of users who leave in five days
end_in_five_days.py
