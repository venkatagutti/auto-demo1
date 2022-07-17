from Libraries import config_ops
from Libraries import api_ops
from Libraries import verification_ops
from Libraries import log_ops


def test_api_test_1():
    log_ops.add_to_log('Starting API test 1')
    request_url = f'{config_ops.get_base_api_url()}/api/users?page=2'
    resp = api_ops.api_get(endpoint=request_url, headers=None, payload=None)
    verification_ops.text_contains(text_to_find='michael.lawson@reqres.in', full_text=resp.text)
    log_ops.add_to_log('Completed API test 1')


def test_api_test_2():
    log_ops.add_to_log('Starting API test 2')
    request_url = f'{config_ops.get_base_api_url()}/api/users?page=2'
    resp = api_ops.api_get(endpoint=request_url, headers=None, payload=None)
    user_id = [usr['id'] for usr in resp.json()['data'] if usr['email'] == 'michael.lawson@reqres.in'][0]
    verification_ops.are_equal(expected_result=7, actual_result=user_id)
    log_ops.add_to_log('Completed API test 2')
