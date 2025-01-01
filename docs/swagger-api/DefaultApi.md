# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_code**](DefaultApi.md#evaluate_code) | **POST** /evaluate | Evaluate the correctness and efficiency of the generated code
[**generate_code**](DefaultApi.md#generate_code) | **POST** /generate | Generate Python code based on a user prompt
[**refactor_code**](DefaultApi.md#refactor_code) | **POST** /refactor | Refactor the code based on feedback

# **evaluate_code**
> InlineResponse2001 evaluate_code(body)

Evaluate the correctness and efficiency of the generated code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.EvaluateBody() # EvaluateBody | 

try:
    # Evaluate the correctness and efficiency of the generated code
    api_response = api_instance.evaluate_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluate_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvaluateBody**](EvaluateBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_code**
> InlineResponse200 generate_code(body)

Generate Python code based on a user prompt

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.GenerateBody() # GenerateBody | 

try:
    # Generate Python code based on a user prompt
    api_response = api_instance.generate_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateBody**](GenerateBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refactor_code**
> InlineResponse2002 refactor_code(body)

Refactor the code based on feedback

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.RefactorBody() # RefactorBody | 

try:
    # Refactor the code based on feedback
    api_response = api_instance.refactor_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refactor_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefactorBody**](RefactorBody.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

