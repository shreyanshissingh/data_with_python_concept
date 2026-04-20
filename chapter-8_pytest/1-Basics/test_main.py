from main import Weather

def test_is_hot():
    weather = Weather(temp=35, rain_probability=0.2)
    assert weather.is_hot() == True
    assert weather.is_rainy() == False
    
    weather = Weather(temp=55, rain_probability=0.2)
    assert weather.is_hot() == True
    assert weather.is_rainy() == False

def test_is_not_hot():
    weather = Weather(temp=25, rain_probability=0.6)
    assert weather.is_hot() == False
    assert weather.is_rainy() == True


