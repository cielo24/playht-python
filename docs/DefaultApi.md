# playht.DefaultApi

All URIs are relative to *https://api.play.ht*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloned_voices**](DefaultApi.md#cloned_voices) | **GET** /api/v2/cloned-voices | Obtains a list of all cloned voices created by the user.
[**convert_ssml_to_speech**](DefaultApi.md#convert_ssml_to_speech) | **POST** /api/v1/convert | Convert SSML to Speech. It can generate text for Standard &amp; Premium (S&amp;P) voices. The identifiers for these voices look like &#x27;en-US-JennyNeural&#x27;. If you are using PlayHT voices (their identifiers look like &#x27;larry&#x27; or a URL).
[**create_instant_voice_clone_url**](DefaultApi.md#create_instant_voice_clone_url) | **POST** /api/v2/cloned-voices/instant/ | Create Instant Voice Clone (via file URL). Create an instant voice clone by providing an URL for a sample audio file.
[**delete_cloned_voices**](DefaultApi.md#delete_cloned_voices) | **DELETE** /api/v2/cloned-voices | Delete Cloned Voices. Deletes a cloned voice created by the user using the provided voice_id.
[**get_conversion_job_status**](DefaultApi.md#get_conversion_job_status) | **GET** /api/v1/articleStatus | Get conversion job status. Gets text-to-speech job status and generated audio file URL.
[**sp_voices**](DefaultApi.md#sp_voices) | **GET** /api/v1/getVoices | Gets the full list of Standard &amp; Premium (S&amp;P) voices.
[**voices**](DefaultApi.md#voices) | **GET** /api/v2/voices | Gets the full list of stock PlayHT Voices available for use with the API.

# **cloned_voices**
> list[ClonedVoiceResponse] cloned_voices()

Obtains a list of all cloned voices created by the user.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))

try:
    # Obtains a list of all cloned voices created by the user.
    api_response = api_instance.cloned_voices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cloned_voices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClonedVoiceResponse]**](ClonedVoiceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_ssml_to_speech**
> SSMLConversionResponse convert_ssml_to_speech(body=body)

Convert SSML to Speech. It can generate text for Standard & Premium (S&P) voices. The identifiers for these voices look like 'en-US-JennyNeural'. If you are using PlayHT voices (their identifiers look like 'larry' or a URL).

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))
body = playht.SSMLConversionPayload() # SSMLConversionPayload |  (optional)

try:
    # Convert SSML to Speech. It can generate text for Standard & Premium (S&P) voices. The identifiers for these voices look like 'en-US-JennyNeural'. If you are using PlayHT voices (their identifiers look like 'larry' or a URL).
    api_response = api_instance.convert_ssml_to_speech(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->convert_ssml_to_speech: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SSMLConversionPayload**](SSMLConversionPayload.md)|  | [optional]

### Return type

[**SSMLConversionResponse**](SSMLConversionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_instant_voice_clone_url**
> SSMLConversionResponse create_instant_voice_clone_url(sample_file_url, voice_name)

Create Instant Voice Clone (via file URL). Create an instant voice clone by providing an URL for a sample audio file.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))
sample_file_url = 'sample_file_url_example' # str | The URL of the audio file selected as the source for the voice clone. The file should have a duration ranging from 2 seconds to 1 hour. It can be in any audio format, as long as it falls within the size range of 5kb to 50 MB
voice_name = 'voice_name_example' # str | The name for this new cloned voice.

try:
    # Create Instant Voice Clone (via file URL). Create an instant voice clone by providing an URL for a sample audio file.
    api_response = api_instance.create_instant_voice_clone_url(sample_file_url, voice_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_instant_voice_clone_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_file_url** | **str**| The URL of the audio file selected as the source for the voice clone. The file should have a duration ranging from 2 seconds to 1 hour. It can be in any audio format, as long as it falls within the size range of 5kb to 50 MB |
 **voice_name** | **str**| The name for this new cloned voice. |

### Return type

[**SSMLConversionResponse**](SSMLConversionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloned_voices**
> delete_cloned_voices(voice_id)

Delete Cloned Voices. Deletes a cloned voice created by the user using the provided voice_id.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))
voice_id = 'voice_id_example' # str | The ID of the cloned voice to be deleted.

try:
    # Delete Cloned Voices. Deletes a cloned voice created by the user using the provided voice_id.
    api_instance.delete_cloned_voices(voice_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cloned_voices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**| The ID of the cloned voice to be deleted. |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversion_job_status**
> ConversionJobStatusResponse get_conversion_job_status(transcription_id)

Get conversion job status. Gets text-to-speech job status and generated audio file URL.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))
transcription_id = 'transcription_id_example' # str | Transcription ID

try:
    # Get conversion job status. Gets text-to-speech job status and generated audio file URL.
    api_response = api_instance.get_conversion_job_status(transcription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_conversion_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_id** | **str**| Transcription ID |

### Return type

[**ConversionJobStatusResponse**](ConversionJobStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sp_voices**
> SPVoiceResponse sp_voices()

Gets the full list of Standard & Premium (S&P) voices.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))

try:
    # Gets the full list of Standard & Premium (S&P) voices.
    api_response = api_instance.sp_voices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sp_voices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SPVoiceResponse**](SPVoiceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voices**
> list[VoiceResponse] voices()

Gets the full list of stock PlayHT Voices available for use with the API.

### Example
```python
from __future__ import print_function
import time
import playht
from playht.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = playht.Configuration()
configuration.api_key['AUTHORIZATION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTHORIZATION'] = 'Bearer'
# Configure API key authorization: UserAuth
configuration = playht.Configuration()
configuration.api_key['X-USER-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-USER-ID'] = 'Bearer'

# create an instance of the API class
api_instance = playht.DefaultApi(playht.ApiClient(configuration))

try:
    # Gets the full list of stock PlayHT Voices available for use with the API.
    api_response = api_instance.voices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->voices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VoiceResponse]**](VoiceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

