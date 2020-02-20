from hashlib import sha256


def get_hexdigest(salt, password):
	returh sha256(salt+password).hexdigest()

get_hexdigest('reddit', 'p@ssw0rd')