import unittest
from unittest.mock import Mock, patch
import get_status

class TestSubmitRequest(unittest.TestCase):
    @patch('get_status.requests.get')
    def test_submit_request_connection_refused_error(self, mock_obj):
        mock_obj.return_value.status_code = 429
        # check error
        with self.assertRaises(ConnectionError) as exception_context:
            get_status.get_status('', {}, {})
        self.assertEqual(
            str(exception_context.exception),
            'Request returned a status other than 200: 429'
        )

