# coding: utf-8

"""
    PlayHT API

    The PlayHT's API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devs@play.ht
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SSMLConversionResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'str',
        'transcription_id': 'str',
        'content_length': 'float',
        'word_count': 'float'
    }

    attribute_map = {
        'status': 'status',
        'transcription_id': 'transcriptionId',
        'content_length': 'contentLength',
        'word_count': 'wordCount'
    }

    def __init__(self, status=None, transcription_id=None, content_length=None, word_count=None):  # noqa: E501
        """SSMLConversionResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._transcription_id = None
        self._content_length = None
        self._word_count = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if transcription_id is not None:
            self.transcription_id = transcription_id
        if content_length is not None:
            self.content_length = content_length
        if word_count is not None:
            self.word_count = word_count

    @property
    def status(self):
        """Gets the status of this SSMLConversionResponse.  # noqa: E501

        Status of the conversion.  # noqa: E501

        :return: The status of this SSMLConversionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SSMLConversionResponse.

        Status of the conversion.  # noqa: E501

        :param status: The status of this SSMLConversionResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def transcription_id(self):
        """Gets the transcription_id of this SSMLConversionResponse.  # noqa: E501

        This is the ID you need to use to poll the status of the audio file in the Get Article Conversion Status endpoint.  # noqa: E501

        :return: The transcription_id of this SSMLConversionResponse.  # noqa: E501
        :rtype: str
        """
        return self._transcription_id

    @transcription_id.setter
    def transcription_id(self, transcription_id):
        """Sets the transcription_id of this SSMLConversionResponse.

        This is the ID you need to use to poll the status of the audio file in the Get Article Conversion Status endpoint.  # noqa: E501

        :param transcription_id: The transcription_id of this SSMLConversionResponse.  # noqa: E501
        :type: str
        """

        self._transcription_id = transcription_id

    @property
    def content_length(self):
        """Gets the content_length of this SSMLConversionResponse.  # noqa: E501

        Length of the converted content.  # noqa: E501

        :return: The content_length of this SSMLConversionResponse.  # noqa: E501
        :rtype: float
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this SSMLConversionResponse.

        Length of the converted content.  # noqa: E501

        :param content_length: The content_length of this SSMLConversionResponse.  # noqa: E501
        :type: float
        """

        self._content_length = content_length

    @property
    def word_count(self):
        """Gets the word_count of this SSMLConversionResponse.  # noqa: E501

        Number of words in the converted content.  # noqa: E501

        :return: The word_count of this SSMLConversionResponse.  # noqa: E501
        :rtype: float
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this SSMLConversionResponse.

        Number of words in the converted content.  # noqa: E501

        :param word_count: The word_count of this SSMLConversionResponse.  # noqa: E501
        :type: float
        """

        self._word_count = word_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SSMLConversionResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SSMLConversionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other