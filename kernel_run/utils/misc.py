import random
import string
import re
import os

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


DEFAULT_PREFIX = 'kr/'


def gen_hash(len=5):
    """Create a random alphanumeric hash of a given length"""
    return ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in xrange(len)])


def slugify(title):
    """Convert a title into a URL slug"""
    return re.sub(r'\W+', '-', title.lower()).replace('_', '-')


url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def is_url(str):
    """Check if given string is a URL"""
    return re.match(url_regex, str) is not None


def url_filename(url):
    """Extract the filename from URL (if present)"""
    path = urlparse(url).path
    fname = os.path.basename(path)
    if not fname:
        fname = "notebook-" + gen_hash()
    return fname
