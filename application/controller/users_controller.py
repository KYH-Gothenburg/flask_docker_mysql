import json

import data.repository.user_repository as user_repo

def get_all_users_json():
    users = get_all_users()
    converted = [user.to_dict() for user in users]
    return json.dumps(converted)


def get_all_users():
    return user_repo.get_all_users()

