import os

CLIENT_ID = os.environ.get("CLIENT_ID") # Application (client) ID of app registration

CLIENT_SECRET = os.environ.get("CLIENT_SECRET")   # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = os.environ.get("AUTHORITY")  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

REDIRECT_PATH = os.environ.get("REDIRECT_PATH")  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = os.environ.get("ENDPOINT")  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = [os.environ.get("SCOPE")]

SESSION_TYPE = os.environ.get("SESSION_TYPE")  # Specifies the token cache should be stored in server-side session

if None in (CLIENT_ID, CLIENT_SECRET, AUTHORITY, REDIRECT_PATH,
    ENDPOINT, SESSION_TYPE) or len(SCOPE) == 0:
    raise Exception("You are lacking a few environment variables needed to run")