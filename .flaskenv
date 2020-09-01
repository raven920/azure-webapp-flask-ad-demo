#FOR INFO REGARDING THIS ENV VARIABLES CHECK "lamejorwebapp/app_config.py"
#fill in your Azure AD APP info:

CLIENT_ID="" 
CLIENT_SECRET="" 
AUTHORITY="https://login.microsoftonline.com/common" 
REDIRECT_PATH="/getAToken" 
ENDPOINT='https://graph.microsoft.com/v1.0/users'
SCOPE="User.ReadBasic.All"

#FLASK SESSION TYPE
SESSION_TYPE="filesystem" 