import json

GET, POST, PUT, PATCH, DELETE, HEADER, BODY, RESPONSE = 'GET,POST,PUT,PATCH,DELETE,HEADER,BODY,RESPONSE'.split(',')
ENDPOINT_INDEX = 0


def is_request(text: str) -> bool:
    first = text.split()[0]
    return first in [GET, POST, PUT, PATCH, DELETE]


def find_index(array: list, needle: str) -> int:
    for index, item in enumerate(array):
        if needle in item:
            return index
    return -1


def html_query_to_dict(query: str) -> dict:
    output = {}
    for row in query.split('&'):
        key, val = row.split('=')
        output[key] = val
    return output


def convert_request_to_dict(input: str) -> dict:
    output = {}
    lines = input.split('\n')
    while '' in lines:
        lines.remove('')

    method, url = lines[ENDPOINT_INDEX].split()
    lines.pop(ENDPOINT_INDEX)
    output['endpoint'] = {'method': method, 'url': url}

    BODY_INDEX = find_index(lines, BODY)
    if BODY_INDEX > -1:
        lines.pop(BODY_INDEX)
        body = lines[BODY_INDEX]
        lines.pop(BODY_INDEX)
        if method == GET:
            output['body'] = html_query_to_dict(body)
        else:
            output['body'] = json.loads(body)

    RESPONSE_INDEX = find_index(lines, RESPONSE)
    if RESPONSE_INDEX > -1:
        output['status_code'] = lines[RESPONSE_INDEX].split()[-1]
        lines.pop(RESPONSE_INDEX)
        response = lines[RESPONSE_INDEX]
        lines.pop(RESPONSE_INDEX)
        output['response'] = json.loads(response)

    if HEADER in lines:
        lines.remove(HEADER)
        output['headers'] = {}
        for line in lines:
            key, val = line.split(':')
            output['headers'][key] = val

    return output


if __name__ == '__main__':
    BASE_DIR: str = ''
    input: str = open(BASE_DIR + 'request.txt').read()
    output: dict = convert_request_to_dict(input)
    open(BASE_DIR + 'request.json', '+w').write(json.dumps(output))
    print(json.dumps(output, ensure_ascii=False, indent=2))
