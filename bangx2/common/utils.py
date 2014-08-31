import hashlib
from bangx2.settings import MD5_SEED


def get_md5(s):
    if s:
        m = hashlib.md5(s)
        m.update(MD5_SEED)
        return m.hexdigest()
    else:
        return None
