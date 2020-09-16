import jwt
from django.conf import settings
from rest_framework import exceptions
from django.utils.translation import ugettext as _

JWT_ALGORITHM = 'HS256'


def encode(payload):
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm=JWT_ALGORITHM)
    except jwt.ExpiredSignature:
        msg = _('Signature has expired.')
        raise exceptions.AuthenticationFailed(msg)
    except jwt.DecodeError:
        msg = _('Error decoding signature.')
        raise exceptions.AuthenticationFailed(msg)
    except jwt.InvalidTokenError:
        raise exceptions.AuthenticationFailed()
    return payload
