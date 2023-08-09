# GrantAccessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaxial_id** | **object** |  | 
**user_id** | **object** |  | 

## Example

```python
from coaxial.models.grant_access_request import GrantAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantAccessRequest from a JSON string
grant_access_request_instance = GrantAccessRequest.from_json(json)
# print the JSON string representation of the object
print GrantAccessRequest.to_json()

# convert the object into a dict
grant_access_request_dict = grant_access_request_instance.to_dict()
# create an instance of GrantAccessRequest from a dict
grant_access_request_form_dict = grant_access_request.from_dict(grant_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


