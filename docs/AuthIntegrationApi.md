# coaxial.AuthIntegrationApi

All URIs are relative to *https://api.coaxial.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrate_okta**](AuthIntegrationApi.md#integrate_okta) | **POST** /auth_integration/okta/init | Integrate Okta
[**list_auth_integrations**](AuthIntegrationApi.md#list_auth_integrations) | **GET** /auth_integration/list | List auth integrations
[**list_users**](AuthIntegrationApi.md#list_users) | **GET** /users/list | List users


# **integrate_okta**
> IntegrateOktaResponse integrate_okta(integrate_okta_request)

Integrate Okta

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_okta_request import IntegrateOktaRequest
from coaxial.models.integrate_okta_response import IntegrateOktaResponse
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
    api_instance = coaxial.AuthIntegrationApi(api_client)
    integrate_okta_request = coaxial.IntegrateOktaRequest() # IntegrateOktaRequest | 

    try:
        # Integrate Okta
        api_response = api_instance.integrate_okta(integrate_okta_request)
        print("The response of AuthIntegrationApi->integrate_okta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthIntegrationApi->integrate_okta: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_okta_request** | [**IntegrateOktaRequest**](IntegrateOktaRequest.md)|  | 

### Return type

[**IntegrateOktaResponse**](IntegrateOktaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index names in an array of strings |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_integrations**
> ListAuthIntegrationsResponse list_auth_integrations()

List auth integrations

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.list_auth_integrations_response import ListAuthIntegrationsResponse
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
    api_instance = coaxial.AuthIntegrationApi(api_client)

    try:
        # List auth integrations
        api_response = api_instance.list_auth_integrations()
        print("The response of AuthIntegrationApi->list_auth_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthIntegrationApi->list_auth_integrations: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAuthIntegrationsResponse**](ListAuthIntegrationsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users()

List users

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.list_users_response import ListUsersResponse
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
    api_instance = coaxial.AuthIntegrationApi(api_client)

    try:
        # List users
        api_response = api_instance.list_users()
        print("The response of AuthIntegrationApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthIntegrationApi->list_users: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

