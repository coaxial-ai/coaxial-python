# AuthIntegration

The AuthConnector model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **object** |  | 

## Example

```python
from coaxial.models.auth_integration import AuthIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthIntegration from a JSON string
auth_integration_instance = AuthIntegration.from_json(json)
# print the JSON string representation of the object
print AuthIntegration.to_json()

# convert the object into a dict
auth_integration_dict = auth_integration_instance.to_dict()
# create an instance of AuthIntegration from a dict
auth_integration_form_dict = auth_integration.from_dict(auth_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


