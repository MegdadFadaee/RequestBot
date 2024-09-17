import os

import requests


class LiaraApi:
    BASE_URL = 'https://api.iran.liara.ir'
    LIARA_TOKEN = os.environ.get('LIARA_TOKEN')
    CURRENT_PROJECT = os.environ.get('CURRENT_PROJECT')
    headers = {
        'Authorization': 'Bearer ' + LIARA_TOKEN
    }

    @staticmethod
    def url(uri: str) -> str:
        return f'{LiaraApi.BASE_URL}{uri}'

    @staticmethod
    def get_me() -> dict:
        return requests.get(LiaraApi.url('/v1/me'), headers=LiaraApi.headers).json()

    @staticmethod
    def get_projects_releases(package_name: str) -> dict:
        return requests.get(LiaraApi.url(f'/v1/projects/{package_name}/releases'), headers=LiaraApi.headers).json()

    @staticmethod
    def get_current_releases() -> dict:
        releases: dict = LiaraApi.get_projects_releases(LiaraApi.CURRENT_PROJECT)
        releases['releases'] = len(releases['releases'])
        return releases

    @staticmethod
    def is_release_command(command: str) -> bool:
        return command.startswith('/release') and LiaraApi.CURRENT_PROJECT in command


if __name__ == '__main__':
    import json

    print(json.dumps(LiaraApi.get_me(), ensure_ascii=False, indent=4))
