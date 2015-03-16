PROJECT_APPS = ('accounts', 'AngularJS-Django',)

THIRD_PARTY_APPS = (
  'social.apps.django_app.default', #python-social-auth for facebook authentication:
  'django_extensions', #django_extensions for getting better debug on runserver dev mode only
  'rest_framework', #tools for providing a restful api for data models.
  'corsheaders',
)

# Not yet implemented.  Take from above (third party apps) and below (libraries)
# and generate + install a requirements.txt via pip.
LIBRARIES = ('',)
