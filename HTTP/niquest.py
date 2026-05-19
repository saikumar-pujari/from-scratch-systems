import niquest
response=niquest.get(url="ttps://jsonplaceholder.typicode.com/posts/1")
print(response)
print(response)
print(response.status_code)
print(response.text)
print(response.json())

