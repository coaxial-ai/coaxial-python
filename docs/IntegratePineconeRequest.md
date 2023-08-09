# IntegratePineconeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **object** |  | 
**environment** | **object** |  | 

## Example

```python
from coaxial.models.integrate_pinecone_request import IntegratePineconeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegratePineconeRequest from a JSON string
integrate_pinecone_request_instance = IntegratePineconeRequest.from_json(json)
# print the JSON string representation of the object
print IntegratePineconeRequest.to_json()

# convert the object into a dict
integrate_pinecone_request_dict = integrate_pinecone_request_instance.to_dict()
# create an instance of IntegratePineconeRequest from a dict
integrate_pinecone_request_form_dict = integrate_pinecone_request.from_dict(integrate_pinecone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


