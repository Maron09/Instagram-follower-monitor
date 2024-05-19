import instaloader

def get_follower_count(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.followers


