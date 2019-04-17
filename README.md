# Lyft-Internship

## How to install dependancies

1. Create a virtual environment:

   `python3 -m venv api_env`
   I have called the folder that contains the virtual environment api_env.

2. Enter the vitual environment:
   `source api_env/bin/activate`

3. Install the dependencies from requirements.txt:
   `pip3 install -r requirements.txt`

## How to start the api

The api is made with python/flask stack. The api was built so it will listen to port 5000 on the localhost. To start the api, run the app.py file with python3:
`python3 app.py`

## Passing data to the api

Since the api is set to localhost and port 5000, you can run the bottom command below to test the api:

`curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'`

## How the /test route works:

The api is set to accept a POST request to the route “/test” which looks for the key "string_to_cut" and uses its value. If the key exists, then the function in the "/test" route will parse the string in the value, take every three letters, and saves it into a JSON object with the key "return_string".

So, for the above example, the returned JSON object should be:
`{"return_string":"muydv"}`.

If the string passed is less than 3 letters, the route will return an empty string:
`{"return_string":""}`.

## Author

Andrew Suh
