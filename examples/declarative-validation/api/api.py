from chilo_api import Chilo

from api.common import auth


api = Chilo(
    base_path='/basic/v1',
    handlers='api/handlers/',
    openapi='api/openapi.yml',
    when_auth_required=auth.authorize,
)