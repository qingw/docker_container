# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ArtistNotFound(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None):
        """
        ArtistNotFound - a model defined in Swagger

        :param code: The code of this ArtistNotFound.
        :type code: str
        :param message: The message of this ArtistNotFound.
        :type message: str
        """
        self.swagger_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ArtistNotFound':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The artistNotFound of this ArtistNotFound.
        :rtype: ArtistNotFound
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """
        Gets the code of this ArtistNotFound.

        :return: The code of this ArtistNotFound.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """
        Sets the code of this ArtistNotFound.

        :param code: The code of this ArtistNotFound.
        :type code: str
        """
        allowed_values = ["artist_name"]
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self) -> str:
        """
        Gets the message of this ArtistNotFound.

        :return: The message of this ArtistNotFound.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this ArtistNotFound.

        :param message: The message of this ArtistNotFound.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

