# Copyright 2024-2025 Canonical Ltd.  This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

from maasservicelayer.models.base import MaasTimestampedBaseModel, make_builder


class VmCluster(MaasTimestampedBaseModel):
    pass


VmClusterBuilder = make_builder(VmCluster)
