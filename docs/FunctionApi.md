# coaxial.FunctionApi

All URIs are relative to *https://api.coaxial.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrate_function**](FunctionApi.md#integrate_function) | **POST** /functions/create | Integrate model functions
[**list_functions**](FunctionApi.md#list_functions) | **GET** /functions/list/ | List model functions
[**remove_function**](FunctionApi.md#remove_function) | **POST** /functions/remove | Remove model functions


# **integrate_function**
> IntegrateFunctionResponse integrate_function(integrate_function_request)

Integrate model functions

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_function_request import IntegrateFunctionRequest
from coaxial.models.integrate_function_response import IntegrateFunctionResponse
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
    api_instance = coaxial.FunctionApi(api_client)
    integrate_function_request = coaxial.IntegrateFunctionRequest() # IntegrateFunctionRequest | 

    try:
        # Integrate model functions
        api_response = api_instance.integrate_function(integrate_function_request)
        print("The response of FunctionApi->integrate_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionApi->integrate_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_function_request** | [**IntegrateFunctionRequest**](IntegrateFunctionRequest.md)|  | 

### Return type

[**IntegrateFunctionResponse**](IntegrateFunctionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The function information (including its id) |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_functions**
> ListFunctionsResponse list_functions(user_id=user_id)

List model functions

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.list_functions_response import ListFunctionsResponse
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
    api_instance = coaxial.FunctionApi(api_client)
    user_id = None # object |  (optional)

    try:
        # List model functions
        api_response = api_instance.list_functions(user_id=user_id)
        print("The response of FunctionApi->list_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionApi->list_functions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**ListFunctionsResponse**](ListFunctionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_function**
> RemoveFunctionResponse remove_function(remove_function_request)

Remove model functions

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.remove_function_request import RemoveFunctionRequest
from coaxial.models.remove_function_response import RemoveFunctionResponse
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
    api_instance = coaxial.FunctionApi(api_client)
    remove_function_request = coaxial.RemoveFunctionRequest() # RemoveFunctionRequest | 

    try:
        # Remove model functions
        api_response = api_instance.remove_function(remove_function_request)
        print("The response of FunctionApi->remove_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionApi->remove_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_function_request** | [**RemoveFunctionRequest**](RemoveFunctionRequest.md)|  | 

### Return type

[**RemoveFunctionResponse**](RemoveFunctionResponse.md)

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

