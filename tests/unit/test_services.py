import pytest
from fastapi.exceptions import HTTPException

from services import get_city_coordinates


@pytest.mark.parametrize("city, expected_coordinates", [
    ("London", True),
    ("New York", True),
    ("Dream City23", False)
])
async def test_get_city_coordinates_success(city, expected_coordinates):
    if not expected_coordinates:
        with pytest.raises(HTTPException) as excinfo:
            get_city_coordinates(city)
        assert str(excinfo.value) == "404: City not found"
    else:
        assert type(get_city_coordinates(city)) == tuple
