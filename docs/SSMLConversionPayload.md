# SSMLConversionPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssml** | **list[str]** | Array of strings, where each string represents a paragraph in SSML format. | 
**voice** | **str** | Voice used to synthesize the text. | 
**title** | **str** | A name to your file. You can use this name to find the audio in your Play.ht dashboard. | [optional] 
**narration_style** | **str** | String representing the tone and accent of the voice to read the text. Make sure the value for narrationStyle is supported by the voice in your request. | [optional] 
**global_speed** | **str** | String in the format &lt;number&gt;%, where &lt;number&gt; is in the closed interval of [20, 200]. Use this to speed-up, or slow-down the speaking rate of the speech. | [optional] 
**pronunciations** | [**list[SSMLConversionPayloadPronunciations]**](SSMLConversionPayloadPronunciations.md) | Array of objects to handle specific word pronunciations. | [optional] 
**trim_silence** | **bool** | When enabled, the audio will be trimmed to remove any silence from the end of the file. | [optional] 
**transcription_id** | **str** | Pass this to update an existing audio file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

