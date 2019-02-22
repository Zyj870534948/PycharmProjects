import homeassistant.remote as remote

api = remote.API('192.168.3.21', 'yumu1234')
print(remote.validate_api(api))

