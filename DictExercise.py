person = {"name":"Ayush Gupta","gender":"Male","age":24,"address":"NewDelhi","phone":8745056594}
query = input("What information you want to fetch : ").lower()
result=person.get(query,"Not Found")
print(result)
