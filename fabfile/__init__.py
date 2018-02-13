from . import common
from . import install

from fabric.state import env

env.repository = "https://github.com/aibaq/test_django"
env.repository_ssh = "git@github.com:aibaq/test_django"
env.repo_name = "test_django"
env.user = "ubuntu"
env.key_filename = "~/test_django.pem"
env.hosts = [""]
