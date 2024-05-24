DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_database_name',  # Replace with your MongoDB database name
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://shaikhaamir056:lG0sTEUlMKdGuTK8@cluster0.pbgdegq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
            'port': 27017,
            'username': 'shaikhaamir056',
            'password': 'lG0sTEUlMKdGuTK8',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        },
    }
}