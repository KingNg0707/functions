🎉🙌 Thank you so much, ChatGPT! 🙏🤖 You are amazing! 🚀🌟 Your help in creating this README is greatly appreciated. 🙌🎉

# LoadJson
</code></div></div></pre>

LoadJson is a Python class that provides a simple way to load JSON data from a URL or a local file and access specific elements of the JSON object.

## Installation

No installation is required. The LoadJson class can be used directly in your Python code by importing the `LoadJson` class from the `loadjson.py` module.

## Usage

1. Import the `LoadJson` class from the `loadjson.py` module.
```python
from loadjson import LoadJson
```

2. Create a `LoadJson` object by providing the path or URL of the JSON data and a boolean flag that indicates whether the path is a URL or a local file.
```python
load_json = LoadJson("http://localhost:8080/config_server.json", True)
```

3. Access specific elements of the JSON object using the `load_from_id` or `load_from_id_dict` methods, which take an identifier as input and return the corresponding JSON object. The `load_from_id_dict` method returns a dictionary object while the `load_from_id` method returns an object that can be accessed using dot notation.
```python
this = load_json.load_from_id_dict("xxxx1")
print(this["Working_Time"]["Start"])
```

4. When loading JSON data from a local file, set the boolean flag to `False` and provide the path to the file.
```python
load_json = LoadJson("path_to/config_server.json", False)
```

## Dependencies

The LoadJson class requires the following Python modules:
- `json`
- `urllib.request` (for loading JSON from a URL)

## License

This code is released under the MIT License.
