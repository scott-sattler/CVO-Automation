import os
from dotenv import load_dotenv
load_dotenv()

# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# You can configure your authority via environment variable
# Defaults to a multi-tenant app in world-wide cloud
AUTHORITY = os.getenv("AUTHORITY", "https://login.microsoftonline.com/common")

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# WORKING TEST
DRIVE_ID = os.getenv("DRIVE_ID")
WEB_ID = os.getenv("WEB_ID")
SITE_ID = os.getenv("SITE_ID")
ITEM_ID = os.getenv("ITEM_ID")
ENDPOINT_G = os.getenv("ENDPOINT_G")

AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]
# SCOPE = ["User.ReadBasic.All", "offline_access", "openid", "Sites.Read.All", "User.Read", "AllSites.Read", "AllSites.Write"]

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# Using the file system will not work in most production systems,
# it's better to use a database-backed session store instead.
