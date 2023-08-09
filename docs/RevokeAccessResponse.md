# RevokeAccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **object** |  | 
**user_id** | **object** |  | 

## Example

```python
from coaxial.models.revoke_access_response import RevokeAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAccessResponse from a JSON string
revoke_access_response_instance = RevokeAccessResponse.from_json(json)
# print the JSON string representation of the object
print RevokeAccessResponse.to_json()

# convert the object into a dict
revoke_access_response_dict = revoke_access_response_instance.to_dict()
# create an instance of RevokeAccessResponse from a dict
revoke_access_response_form_dict = revoke_access_response.from_dict(revoke_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


