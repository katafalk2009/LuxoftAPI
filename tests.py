import pytest
import main
def test_resource_code():
    assert main.get_page_data(main.FILMS_URL) == 200

