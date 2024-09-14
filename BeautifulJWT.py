from jwt import JWT

Bearer, Authorization = 'Bearer,Authorization'.split(',')


class BeautifulJWT(JWT):

    @staticmethod
    def is_jwt_token(message: str) -> bool:
        return message.startswith(Bearer) or message.startswith(Authorization)

    @staticmethod
    def decode_without_verify(jwt_token: str) -> dict:
        return JWT().decode(jwt_token, do_verify=False)
