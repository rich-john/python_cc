current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['admin', 'user5', 'user6', 'user7', 'user8']
current_users_lower = [user.lower() for user in current_users]
new_users_lower = [user.lower() for user in new_users]
for new_user in new_users_lower:
    if new_user in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"Great! {new_user} is available.")
        