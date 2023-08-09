# RevokeAccessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaxial_id** | **object** |  | 
**user_id** | **object** |  | 

## Example

```python
from coaxial.models.revoke_access_request import RevokeAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAccessRequest from a JSON string
revoke_access_request_instance = RevokeAccessRequest.from_json(json)
# print the JSON string representation of the object
print RevokeAccessRequest.to_json()

# convert the object into a dict
revoke_access_request_dict = revoke_access_request_instance.to_dict()
# create an instance of RevokeAccessRequest from a dict
revoke_access_request_form_dict = revoke_access_request.from_dict(revoke_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


