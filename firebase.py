import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# config = {
#     "apiKey": "AIzaSyCzV5w_NFXWV2r18ocdk29MPfQfoYFDeGQ",
#     "authDomain": "crud-python-15a0e.firebaseapp.com",
#     "projectId": "crud-python-15a0e",
#     "storageBucket": "crud-python-15a0e.appspot.com",
#     "messagingSenderId": "808333181026",
#     "appId": "1:808333181026:web:ce4792a77c89f0d0bbd13b",
#     "measurementId": "G-YWPZ770YP8"
# }

firebase = {
    "type": "service_account",
    "project_id": "crud-python-15a0e",
    "private_key_id": "158aaea9424ad427b542d57c1283873a21d90481",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDudtHK5DEW8PW8\nKexLMFBo6V3yoOUYCN8wDe7de8Lu6KNRraeKyC4q9vC6I69gW6kkvXR6NIW+o+TW\nlMNcCe5Nrbi2Wmi1dc7BFEbulf2WkrIZegBBOKDHS5AhUll4wFaqyibJ17f2ioYC\nx60I43jf3VNM0A//r4QxiD5B3Z3BF1D5fBRosHQKxfMLGuNEc6N2IF4nRov1hfpQ\nMkUkJDZxAx2iYkxtXOs0jMcNGA2TXtXVMCmCUAtDOH8XmfL5gGelkSEvcDyu2/QC\nYPnPl3rwB3m9g4/8qMJC38rpKKxM1hI+zeOMMx8LjihzMiDaP7tGNKADSShYwhH3\nSuiaA9/3AgMBAAECggEALGDffS9HdXoFeW2h5IJKzKN1kPRhfj4UbyiApiZkqjqQ\nPmCfeAP2F5faSAHhHwEf8s7xUNbadxagPVD1JHlSqJEmeYVMzExu3F7uLnOqfG2z\niGs8hebIgR5uZc0iCodc+a7iVhj3ywGPnA/WA3v14E+bs4VbHN3or6En2PEp7SeS\nMKp6PSFi/yZmQRqHuBvn2qHV2dqD/VTIBkUOtgiY90Oy5rGlVo0NSeTtNg8QlmfW\n6W64CfKL11XWTjK0VAQd4wj0Ep+PspuqWQ4eC57rvTHOgSz+250CFzjJKaAahJ9c\ndYY7Wsabt4y7WBmS2YXTyNIqrVOPMrLv09wpcieihQKBgQD+hTaqO9C549EIcvv/\nHkM5i2IRFw34NuArGAW9pog7m/jandsJREn0yJ8tZLNn9oWVxA6FpbGkmOzSCjlG\nHJoEJwjoL8KDYhZyjXmcZ+B0thlyNplvu0QWh8y4kfeu068V+mX0hhA86ONoFAlC\nQEw9oW9obPibCfuEqAPRkgjL+wKBgQDv2bXjwWTXONeQfFW9probQe4oYUkm198d\nOe9zKQkdipt+/MAvf+EFaMkg555dhkE8mRFnu8dYgpxo3eC+L2lNkUIawvaag9nl\n5dw07qBhI/PkTolSNV52z6LtLilbfdXj6UEoa4Gm026mXn1dRZGxlFDG96uKoEk2\nPQxlg+bfNQKBgAmknGyYtZDFa98JFDkXOW7NtBp3qCTWV2nqkBUeYRz5DNWjk2/n\ncXHfxAAhR5bRxT/mXLJ9k5xr2tUeZAse/ErZ+8FoRdNafQU8DPZ7DQr+9znXjbqo\n+qxr2rrHdP3fsUuA4CoChkz4ed0wnSUwcHMJUcJAFq8xEqF1CCgBg2nPAoGBAOPO\nXinSN5sLTALZdP5Kax0Ug8UqkbYo9qrlqf4xDY1XZtU37rmuteTTX6S3GP0vVKrf\nn15tRatVcoVPp/Q7R8L6olSUtHCRptXqejp0IzPgV/eSeG7ybaRfFho76+AQJqTv\nmIlxgpUW4FN4D44VU4ncmtQ/zFhAYQj49ts8an25AoGADm7ez/kl1Ht/QcM7KrgW\nb3cvKDKDECxluSjEVV5Uve6XqSGmQz/L7ijQeRGtn7u5cWcnf7QhETZN1Q+DSsUi\ntiJlnUfQs6aD1K495XVqFkI8CqQYTwGL+j+dOfC0hKo7JNJDLpFzqJ5RwrX8XPbU\n+AmdGuCQ010WSN4z2nIPKGM=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-zka69@crud-python-15a0e.iam.gserviceaccount.com",
    "client_id": "114234293030479670041",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zka69%40crud-python-15a0e.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
