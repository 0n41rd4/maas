#  Copyright 2025 Canonical Ltd.  This software is licensed under the
#  GNU Affero General Public License version 3 (see the file LICENSE).

from maasservicelayer.models.base import MaasTimestampedBaseModel, make_builder


class NotificationDismissal(MaasTimestampedBaseModel):
    user_id: int
    notification_id: int


NotificationDismissalBuilder = make_builder(NotificationDismissal)
