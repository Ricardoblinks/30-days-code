import json

def parse_json_file(file_path):
    try:
        if file_path.endswith('.json'):
            with open(file_path, 'r') as file:
                # Load JSON data from the file
                data = json.load(file)

            # Display all information in the JSON file
            print(json.dumps(data, indent=2))
        else:
            # Assume input is a direct JSON string
            data = json.loads(file_path)
            print(json.dumps(data, indent=2))

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


# Example usage
json_data_example = '''
{
  "user": {
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "posts": [
    {
      "title": "First Post",
      "content": "This is the content of the first post."
    },
    {
      "title": "Second Post",
      "content": "Another post to showcase JSON parsing."
    }
  ]
}
'''

json_file_path = json_data_example
parse_json_file(json_file_path)
