import json

from jwt import JWT
from jwt.exceptions import JWTDecodeError

Bearer, Authorization = 'Bearer,Authorization'.split(',')


class BeautifulJWT(JWT):

    @staticmethod
    def is_jwt_token(message: str) -> bool:
        return message.startswith(Bearer) or message.startswith(Authorization)

    @staticmethod
    def decode_without_verify(jwt_token: str) -> dict:
        jwt_token = jwt_token.replace(' ', '')
        jwt_token = jwt_token.replace('Bearer', '')
        jwt_token = jwt_token.replace('Authorization:', '')
        return JWT().decode(jwt_token, do_verify=False)

    @staticmethod
    def create_readable_jwt(jwt_token: str) -> str:
        try:
            jwt_dict: dict = BeautifulJWT.decode_without_verify(jwt_token)
            return json.dumps(jwt_dict, ensure_ascii=False, indent=4)
        except JWTDecodeError:
            return 'invalid token.'
