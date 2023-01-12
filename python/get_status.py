import requests

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    if omim_status.status_code != 200:
        raise ConnectionError(f'Request returned a status other than 200: {omim_status.status_code}')
    else:
        return(omim_status)

