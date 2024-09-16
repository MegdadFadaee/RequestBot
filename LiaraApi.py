import requests


BASE_URL = 'https://api.iran.liara.ir'
LIARA_TOKEN = os.environ.get('LIARA_TOKEN')

headers = {
	'Authorization': 'Bearer ' + LIARA_TOKEN
}

def url(uri: str) -> str:
	return f'{BASE_URL}{uri}'

def get_me() -> dict:
	return requests.get(url('/v1/me'), headers=headers).json()

def get_projects_releases(package_name: str) -> dict:
    return requests.get(url(f'/v1/projects/{package_name}/releases'), headers=headers).json()

    
if __name__ == '__main__':
	import json
	print(json.dumps(get_me(), ensure_ascii=False, indent=4))