from .config import *


""" User list """
# page = auth.list_users()
# while page:
#     for user in page.users:
#         print('User: ' + user.uid)
#     # Get next batch of users.
#     page = page.get_next_page()


# user = auth.get_user_by_email("jstn.jaring@gmail.com")
# uid = user.uid
custom_token = auth.create_custom_token("jstn.jaring@gmail.com")
auth.verify_id_token(custom_token)

# try:
#     # Verify the ID token while checking if the token is revoked by
#     # passing check_revoked=True.
#     decoded_token = auth.verify_id_token(id_token, check_revoked=True)
#     # Token is valid and not revoked.
#     uid = decoded_token['uid']
#     print("------------ " + uid)
# except auth.RevokedIdTokenError:
#     # Token revoked, inform the user to reauthenticate or signOut().
#     auth.revoke_refresh_tokens(uid)
#     user = auth.get_user(uid)
#     # Convert to seconds as the auth_time in the token claims is in seconds.
#     revocation_second = user.tokens_valid_after_timestamp / 1000
#     print('Tokens revoked at: {0}'.format(revocation_second))
# except auth.InvalidIdTokenError:
#     # Token is invalid
#     pass


print("ASdasdasd " + uid)
