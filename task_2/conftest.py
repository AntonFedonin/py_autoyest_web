import pytest
import requests
import yaml

S = requests.Session()
with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def logIn():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def post_title():
    return 'WebDriver'


@pytest.fixture()
def new_post():
    return S.post(url=data['post_url'], headers={'X-Auth-Token': logIn},
                  data={'title': 'Превед Медвед!', 'description': 'Описание поста',
                          'content': 'Добавим очередной никому не нужный пост'})


@pytest.fixture()
def get_post():
    return 'Превед Медвед!'
