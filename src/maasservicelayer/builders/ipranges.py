# Copyright 2025 Canonical Ltd.  This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

from datetime import datetime
from typing import Union

from pydantic import Field
from pydantic.networks import IPvAnyAddress

from maascommon.enums.ipranges import IPRangeType
from maasservicelayer.models.base import ResourceBuilder, UNSET, Unset


class IPRangeBuilder(ResourceBuilder):
    """Autogenerated from utilities/generate_builders.py.

    You can still add your custom methods here, they won't be overwritten by
    the generated code.
    """

    comment: Union[str, None, Unset] = Field(default=UNSET, required=False)
    created: Union[datetime, Unset] = Field(default=UNSET, required=False)
    end_ip: Union[IPvAnyAddress, Unset] = Field(default=UNSET, required=False)
    id: Union[int, Unset] = Field(default=UNSET, required=False)
    start_ip: Union[IPvAnyAddress, Unset] = Field(
        default=UNSET, required=False
    )
    subnet_id: Union[int, Unset] = Field(default=UNSET, required=False)
    type: Union[IPRangeType, Unset] = Field(default=UNSET, required=False)
    updated: Union[datetime, Unset] = Field(default=UNSET, required=False)
    user_id: Union[int, None, Unset] = Field(default=UNSET, required=False)

    def must_trigger_workflow(self) -> bool:
        if (
            not isinstance(self.start_ip, Unset)
            or not isinstance(self.end_ip, Unset)
            or not isinstance(self.type, Unset)
            or not isinstance(self.subnet_id, Unset)
        ):
            return True
        return False
