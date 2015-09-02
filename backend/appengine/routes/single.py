from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

__author__ = 'bea'

@login_not_required
@no_csrf
def index():
    return TemplateResponse()