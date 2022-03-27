
import firebase_admin
from firebase_admin import credentials, storage
# import firebase
my_dict = {
  "type": "service_account",
  "project_id": "construction-5054c",
  "private_key_id": "d8a231b1ab1b0379e2e216d2886ae56c9bc6666b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDYe/Vy5HqRXv2X\nof8g5J55tv83NWIIa/UemkXDlU+JnuNIK3ZMITGXlmTT1U1qZRsRwSmlj7r6yaBo\nn5+ncDLDI4s8nkCOZQc7dJU/MMJC1cL4HQQArcdYyoyY9L2o8esOQsHiuOEXaaze\nYY8NzI1EwM7yNIQt1Hqx9iO5OcmjYLYfRssKrUIckS4FAeCQPazm/rpuWBDw2rNJ\n7FWwY6iprPuuJtd6ZeUVVWMH7ttNc9HZr/Hb2+c0bvCcm/CZ7pWWjCgzM6KU2eRc\nikN3n9Pre8q6OoRdGf0hTW90MPg+HcF7uUhgAnFxRP0VdIHv5cqgfz1nM4rgKEUx\ndKhPsWNTAgMBAAECggEAOKVC5fPUAIrfB1jLtdMshoO0R0FwK+z3wDC09Ybxv3x0\nU1OQCj6bR+OB8Y38Sk03Zo9pMtmnnuy4TPgLohfxKG96BPwRv1C/MjcAwH6lLjDZ\n6etJu1W9dkXVwUY1BGp8y4f7TLR8rZAovC3B7WXrRyS+YdENDyLskflqgpKU6Osv\ne3kpRJVRX+xtEVk+kWfA5+Un9rv5R8nlkXJ8XLBg1d2RWvHTIViKj7d9qPSCMs6/\nkXoQMGEIh1PQ5MKABw/7IqNs+R0N80MAfM/WjdYwf917PphGvunoNFdgMHmBkSEs\nD1oCzBnQr4G9tv++pE+5SxJMabV/YqiZiHWquwlqLQKBgQD6o0taLvkMsmK7p8ib\nf7cmBz09E2ZMAcHg9+RiKV1icYHFPcfiFASdG3awMbiQw1FSpZS+Juprf5/+YhC8\n/xezTmUusO1WBmqTPYUyhFmjC2P5cBEYhI1xaihJm0LKFalBvfLEc0siyxmtkFCL\navNd8itQVnTJK1dpGSlEf4cRJQKBgQDdHZwr6kXWBMDVvvpRYNXpWset+o9cZM/3\nLlgHuRVYG4Pgb6bUkd0qgOWNdPGFZ7QBjDRRCsGI1oEPtCb5sGksCK7jhrU7LrUB\nqPQaIO/D6XnQQiy+xyPjaKC9YWsC2UGZA8f9s5sO8dmTABtB8b9O3VBMdTjieMve\n7EZqd9qlFwKBgCBCMimaUB2tO/3xG2XAK19uoRgiThFMTJra7P8hWc6Y014ClJ5p\neyqJZV5KF/ox2V6sxxcuRQ+u7nW8Q3E/19oRJf67cOCYlND8ow8cb7kHd0ecf+bK\n8LV/N045+H+wCAfZHczhFfOVdmmbYHKBQm9+AsslRYS62lZBkckqLMUtAoGAEuFg\nYG+Unv2w6Y9xGFnIajCSNEzcyOrixxxx79bh97ABxrxB5oy98c8nyrhdlyKPwEIU\nhYcBl4mZY5niaheiI1xqcosiFneahRXEIicF0hixihLcdz3R1q0sbH9Q/+FFNKea\nABPB/biw91he+3aE+1rybFTmEpB1+Ab8zEKHrOkCgYEA4UzSiWs/Wegrwz6eRPaD\n7xocmQtWoVf3BaD1TMZr0AnaIZ1RI4nH2QRF52Au6KGTdVprvO0nkyIkypNr8SS3\nmdGs+eMq/KHkTNuU4EaP09NtC2Ae+w5/JV9Kk10bsfQ8SGxFbAYQRCJ8w4nSf0/r\nDH7CsMdUGCMPhnoePrxbBg8=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-sgsh9@construction-5054c.iam.gserviceaccount.com",
  "client_id": "102270756464993602028",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-sgsh9%40construction-5054c.iam.gserviceaccount.com"
}


cred = credentials.Certificate(my_dict)
app = firebase_admin.initialize_app(cred, {
       'storageBucket': 'construction-5054c.appspot.com'
})

bucket = storage.bucket(app = app)
# storage1 = firebase.storage()
# storage.child("images/example.jpg").download("img")