from firebase_admin import credentials , initialize_app

cred = credentials.Certificate('firebase/s_key.json')

try:
	initialize_app(cred, {
		'databaseURL': 'https://raspberrypi75955.firebaseio.com/',
		'databaseAuthVariableOverride': {
		'uid': 'laxz-writer'
		}
	})
except Exception as e:
	print(e)
