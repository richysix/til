from unittest.mock import Mock

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    return(omim_status)

requests = Mock()
requests.get.return_value.status_code = 200

omim_status = get_status('https://api.omim.org/api/status', {}, {})
assert omim_status.status_code == 200

