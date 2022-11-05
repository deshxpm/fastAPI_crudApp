# function for validate latitude
def valid_latitude(lat):
    if float(lat) >= -90 and float(lat) <= 90:
        return True
    else: 
        return False

# function for validate longitude
def validate_longitude(lon):
    if float(lon) >= -180 and float(lon) <= 180:
        return True
    else: 
        return False