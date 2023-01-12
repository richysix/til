from unittest.mock import Mock

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    return(omim_status)

def print_args(base_url, headers, params):
    print(base_url, headers, params)
    return(Mock(status_code = 200))

requests = Mock()
requests.get.side_effect = print_args

omim_status = get_status('https://api.omim.org/api/status', {}, {})
assert omim_status.status_code == 200

