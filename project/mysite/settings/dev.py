from .common import *

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ["127.0.0.1"] # NOTE: djanog_debug_toolbar 용 설정 추가

# Graph models 설정
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
