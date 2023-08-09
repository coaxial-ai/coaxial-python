# PineconeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**index** | **object** |  | 

## Example

```python
from coaxial.models.pinecone_info import PineconeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeInfo from a JSON string
pinecone_info_instance = PineconeInfo.from_json(json)
# print the JSON string representation of the object
print PineconeInfo.to_json()

# convert the object into a dict
pinecone_info_dict = pinecone_info_instance.to_dict()
# create an instance of PineconeInfo from a dict
pinecone_info_form_dict = pinecone_info.from_dict(pinecone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


