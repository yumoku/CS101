def is_friend(name: str):
    if name[0] in ['D', 'N']:
        return True
    return False

print(is_friend('Anna'))
