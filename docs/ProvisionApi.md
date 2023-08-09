# coaxial.ProvisionApi

All URIs are relative to *https://api.coaxial.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_access_by_resource_id**](ProvisionApi.md#check_access_by_resource_id) | **POST** /provisions/can_user_access | Check user access by resource id
[**check_access_for_all**](ProvisionApi.md#check_access_for_all) | **POST** /provisions/can_user_access_all | Check user access for many resources
[**grant_access**](ProvisionApi.md#grant_access) | **POST** /provisions/add_to_user | Grant resource access to user
[**revoke_access**](ProvisionApi.md#revoke_access) | **POST** /provisions/remove_from_user | Revoke resource access for user


# **check_access_by_resource_id**
> object check_access_by_resource_id(check_access_by_resource_id_request)

Check user access by resource id

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.check_access_by_resource_id_request import CheckAccessByResourceIdRequest
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.ProvisionApi(api_client)
    check_access_by_resource_id_request = coaxial.CheckAccessByResourceIdRequest() # CheckAccessByResourceIdRequest | 

    try:
        # Check user access by resource id
        api_response = api_instance.check_access_by_resource_id(check_access_by_resource_id_request)
        print("The response of ProvisionApi->check_access_by_resource_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisionApi->check_access_by_resource_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_access_by_resource_id_request** | [**CheckAccessByResourceIdRequest**](CheckAccessByResourceIdRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A boolean describing whether or not user has resource access |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_access_for_all**
> object check_access_for_all(check_access_for_all_request)

Check user access for many resources

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.check_access_for_all_request import CheckAccessForAllRequest
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.ProvisionApi(api_client)
    check_access_for_all_request = coaxial.CheckAccessForAllRequest() # CheckAccessForAllRequest | 

    try:
        # Check user access for many resources
        api_response = api_instance.check_access_for_all(check_access_for_all_request)
        print("The response of ProvisionApi->check_access_for_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisionApi->check_access_for_all: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_access_for_all_request** | [**CheckAccessForAllRequest**](CheckAccessForAllRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_access**
> GrantAccessResponse grant_access(grant_access_request)

Grant resource access to user

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.grant_access_request import GrantAccessRequest
from coaxial.models.grant_access_response import GrantAccessResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.ProvisionApi(api_client)
    grant_access_request = coaxial.GrantAccessRequest() # GrantAccessRequest | 

    try:
        # Grant resource access to user
        api_response = api_instance.grant_access(grant_access_request)
        print("The response of ProvisionApi->grant_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisionApi->grant_access: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_access_request** | [**GrantAccessRequest**](GrantAccessRequest.md)|  | 

### Return type

[**GrantAccessResponse**](GrantAccessResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user id with updated resource access information |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_access**
> RevokeAccessResponse revoke_access(revoke_access_request)

Revoke resource access for user

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.revoke_access_request import RevokeAccessRequest
from coaxial.models.revoke_access_response import RevokeAccessResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.ProvisionApi(api_client)
    revoke_access_request = coaxial.RevokeAccessRequest() # RevokeAccessRequest | 

    try:
        # Revoke resource access for user
        api_response = api_instance.revoke_access(revoke_access_request)
        print("The response of ProvisionApi->revoke_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisionApi->revoke_access: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_access_request** | [**RevokeAccessRequest**](RevokeAccessRequest.md)|  | 

### Return type

[**RevokeAccessResponse**](RevokeAccessResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user id with updated resource information |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

