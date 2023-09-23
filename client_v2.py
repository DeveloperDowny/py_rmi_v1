import Pyro4

def main():
    
    server_uri = "PYRO:obj_92a76ac3eb5648619c4e23e707b29f35@localhost:56690"

    
    remote_object = Pyro4.Proxy(server_uri)

    try:
        
        document = {"name": "John", "age": 30}
        inserted_id = remote_object.insert_document("mycollection", document)
        print("Inserted document ID:", inserted_id)

        
        query = {"name": "John"}
        result = remote_object.find_document("mycollection", query)
        print("Query result:", result)
    except Pyro4.errors.CommunicationError as e:
        print("Error communicating with the server:", e)
    except Pyro4.errors.PyroError as e:
        print("Pyro4 error:", e)

if __name__ == "__main__":
    main()
