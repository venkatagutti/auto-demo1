import requests
from Libraries import verification_ops
from Configuration import constants


def api_get(endpoint: str, headers: object, payload: object):
    if headers is None and payload is None:
        resp = requests.get(url=endpoint)
    elif headers is None and payload is not None:
        resp = requests.get(url=endpoint, json=payload)
    elif headers is not None and payload is None:
        resp = requests.get(url=endpoint, headers=headers)
    else:
        resp = requests.get(url=endpoint, headers=headers, json=payload)
    verification_ops.are_equal(expected_result=constants.API_SUCCESS_STATUS_CODE, actual_result=resp.status_code)
    return resp
