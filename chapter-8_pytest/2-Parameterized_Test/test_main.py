from main import Weather
import pytest

@pytest.mark.parametrize(
    "temp, rain_probability, expected_hot, expected_rainy",[
        (35, 0.2, True, False),
        (55, 0.2, True, False),
        (40, 0.7, True, True)
    ])
def test_is_hot(temp, rain_probability, expected_hot, expected_rainy):
    weather = Weather(temp=temp, rain_probability=rain_probability)
    assert weather.is_hot() == expected_hot
    assert weather.is_rainy() == expected_rainy


@pytest.mark.parametrize(
    "temp, rain_probability, expected_not_hot, expected_not_rainy",[
        (35, 0.2, False, True),
        (55, 0.2, False, True),
        (40, 0.7, False, False)
    ])
def test_is_not_hot(temp, rain_probability, expected_not_hot, expected_not_rainy):
    weather = Weather(temp=temp, rain_probability=rain_probability)
    assert weather.is_hot() != expected_not_hot
    assert weather.is_rainy() != expected_not_rainy


