import email


registerPayload = {
  "email": "abhishek00717@test.com",
  "password": "secret123"
}

invalid_payload = {
  "email": "abhishek00717@test.com",
  "password": "wrongpassword"
}

missing_password = {
    "email": "abhishek00717@test.com"
}

missing_email = {
    "password": "secret123"
}

empty_payload = {
    "email": "",
    "password": ""
}

