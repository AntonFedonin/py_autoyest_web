import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_step1(logIn, post_title):
    result = S.get(url=data['address'], headers={'X-Auth-Token': logIn}, params={'owner': 'notMe'}).json()['data']
    relult_title = [i['title'] for i in result]
    print(relult_title)
    assert post_title in relult_title, "test_step1 FAIL"


def test_step2(logIn, get_post, new_post):
    new_post()
    result = S.get(url=data['address'], headers={'X-Auth-Token': logIn}, params={'owner': 'notMe'}).json()['data']
    relult_title = [i['description'] for i in result]
    print(relult_title)
    assert get_post in relult_title, "test_step2 FAIL"
