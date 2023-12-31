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

class SPVoice(object):
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
        'value': 'str',
        'name': 'str',
        'language': 'str',
        'voice_type': 'str',
        'language_code': 'str',
        'gender': 'str',
        'service': 'str',
        'sample': 'str',
        'styles': 'list[str]',
        'is_kid': 'bool',
        'is_new': 'bool'
    }

    attribute_map = {
        'value': 'value',
        'name': 'name',
        'language': 'language',
        'voice_type': 'voiceType',
        'language_code': 'languageCode',
        'gender': 'gender',
        'service': 'service',
        'sample': 'sample',
        'styles': 'styles',
        'is_kid': 'isKid',
        'is_new': 'isNew'
    }

    def __init__(self, value=None, name=None, language=None, voice_type=None, language_code=None, gender=None, service=None, sample=None, styles=None, is_kid=None, is_new=None):  # noqa: E501
        """SPVoice - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._name = None
        self._language = None
        self._voice_type = None
        self._language_code = None
        self._gender = None
        self._service = None
        self._sample = None
        self._styles = None
        self._is_kid = None
        self._is_new = None
        self.discriminator = None
        self.value = value
        self.name = name
        self.language = language
        self.voice_type = voice_type
        self.language_code = language_code
        self.gender = gender
        self.service = service
        self.sample = sample
        if styles is not None:
            self.styles = styles
        if is_kid is not None:
            self.is_kid = is_kid
        if is_new is not None:
            self.is_new = is_new

    @property
    def value(self):
        """Gets the value of this SPVoice.  # noqa: E501

        Unique ID for S&P voice.  # noqa: E501

        :return: The value of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SPVoice.

        Unique ID for S&P voice.  # noqa: E501

        :param value: The value of this SPVoice.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def name(self):
        """Gets the name of this SPVoice.  # noqa: E501

        The name of the voice.  # noqa: E501

        :return: The name of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SPVoice.

        The name of the voice.  # noqa: E501

        :param name: The name of this SPVoice.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def language(self):
        """Gets the language of this SPVoice.  # noqa: E501

        Descriptive language name.  # noqa: E501

        :return: The language of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SPVoice.

        Descriptive language name.  # noqa: E501

        :param language: The language of this SPVoice.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def voice_type(self):
        """Gets the voice_type of this SPVoice.  # noqa: E501

        Voice type.  # noqa: E501

        :return: The voice_type of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._voice_type

    @voice_type.setter
    def voice_type(self, voice_type):
        """Sets the voice_type of this SPVoice.

        Voice type.  # noqa: E501

        :param voice_type: The voice_type of this SPVoice.  # noqa: E501
        :type: str
        """
        if voice_type is None:
            raise ValueError("Invalid value for `voice_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Standard", "Neural"]  # noqa: E501
        if voice_type not in allowed_values:
            raise ValueError(
                "Invalid value for `voice_type` ({0}), must be one of {1}"  # noqa: E501
                .format(voice_type, allowed_values)
            )

        self._voice_type = voice_type

    @property
    def language_code(self):
        """Gets the language_code of this SPVoice.  # noqa: E501

        Code of the language.  # noqa: E501

        :return: The language_code of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this SPVoice.

        Code of the language.  # noqa: E501

        :param language_code: The language_code of this SPVoice.  # noqa: E501
        :type: str
        """
        if language_code is None:
            raise ValueError("Invalid value for `language_code`, must not be `None`")  # noqa: E501

        self._language_code = language_code

    @property
    def gender(self):
        """Gets the gender of this SPVoice.  # noqa: E501

        Gender of the voice.  # noqa: E501

        :return: The gender of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SPVoice.

        Gender of the voice.  # noqa: E501

        :param gender: The gender of this SPVoice.  # noqa: E501
        :type: str
        """
        if gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")  # noqa: E501
        allowed_values = ["Female", "Male"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def service(self):
        """Gets the service of this SPVoice.  # noqa: E501

        Voice service.  # noqa: E501

        :return: The service of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SPVoice.

        Voice service.  # noqa: E501

        :param service: The service of this SPVoice.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501
        allowed_values = ["polly", "gc", "ms", "watson"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def sample(self):
        """Gets the sample of this SPVoice.  # noqa: E501

        URI with a sample of the voice.  # noqa: E501

        :return: The sample of this SPVoice.  # noqa: E501
        :rtype: str
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this SPVoice.

        URI with a sample of the voice.  # noqa: E501

        :param sample: The sample of this SPVoice.  # noqa: E501
        :type: str
        """
        if sample is None:
            raise ValueError("Invalid value for `sample`, must not be `None`")  # noqa: E501

        self._sample = sample

    @property
    def styles(self):
        """Gets the styles of this SPVoice.  # noqa: E501


        :return: The styles of this SPVoice.  # noqa: E501
        :rtype: list[str]
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this SPVoice.


        :param styles: The styles of this SPVoice.  # noqa: E501
        :type: list[str]
        """

        self._styles = styles

    @property
    def is_kid(self):
        """Gets the is_kid of this SPVoice.  # noqa: E501

        If the voice is from a kid.  # noqa: E501

        :return: The is_kid of this SPVoice.  # noqa: E501
        :rtype: bool
        """
        return self._is_kid

    @is_kid.setter
    def is_kid(self, is_kid):
        """Sets the is_kid of this SPVoice.

        If the voice is from a kid.  # noqa: E501

        :param is_kid: The is_kid of this SPVoice.  # noqa: E501
        :type: bool
        """

        self._is_kid = is_kid

    @property
    def is_new(self):
        """Gets the is_new of this SPVoice.  # noqa: E501

        If the voice is new.  # noqa: E501

        :return: The is_new of this SPVoice.  # noqa: E501
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """Sets the is_new of this SPVoice.

        If the voice is new.  # noqa: E501

        :param is_new: The is_new of this SPVoice.  # noqa: E501
        :type: bool
        """

        self._is_new = is_new

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
        if issubclass(SPVoice, dict):
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
        if not isinstance(other, SPVoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
