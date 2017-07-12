from .common import *

DEBUG = False

INSTALLED_APPS += ['raven.contrib.django.raven_compat', ]  # senty 에러로깅을 위한 추가

# sentry 에러로깅 설정
import raven

GIT_ROOT = os.path.join(BASE_DIR, '..')
if os.path.exists(os.path.join(GIT_ROOT, '.git')):
    release = raven.fetch_git_sha(GIT_ROOT)  # 현재 최근 커밋해시 획득
else:
    release = 'dev'

RAVEN_CONFIG = {
    'release': release,
    'dsn': 'https://b0a8cd152e3c48d3af2dfeae58565ea3:70a0250beaf74aafb7f394fe78ca9d6d@sentry.io/187769',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
}
