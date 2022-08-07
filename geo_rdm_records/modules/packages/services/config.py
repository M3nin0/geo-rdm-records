# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Geo Secretariat.
#
# geo-rdm-records is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""GEO RDM Records Packages API Service configuration."""

from invenio_rdm_records.services import config as rdm_config
from invenio_rdm_records.services.customizations import FromConfig

from ..records.api import GEOPackageDraft, GEOPackageRecord
from .permissions import GEOPackageRecordPermissionPolicy
from .schemas import GEOPackageRecordSchema


class GEOPackageRecordServiceConfig(rdm_config.RDMRecordServiceConfig):
    """GEO Package record draft service config."""

    # Record and draft classes
    record_cls = GEOPackageRecord
    draft_cls = GEOPackageDraft

    # Schemas
    schema = GEOPackageRecordSchema

    # Permission policy
    permission_policy_cls = FromConfig(
        "GEO_RDM_PACKAGE_PERMISSION_POLICY",
        default=GEOPackageRecordPermissionPolicy,
        import_string=True,
    )


class GEOPackageFileRecordServiceConfig(rdm_config.RDMFileRecordServiceConfig):
    """Configuration for package files."""

    # Record class
    record_cls = GEOPackageRecord

    # Permission policy
    permission_policy_cls = FromConfig(
        "GEO_RDM_PACKAGE_PERMISSION_POLICY",
        default=GEOPackageRecordPermissionPolicy,
        import_string=True,
    )


class GEOPackageDraftServiceConfig(rdm_config.RDMFileDraftServiceConfig):
    """Configuration for draft files."""

    # Record class
    record_cls = GEOPackageRecord

    # Permission policy
    permission_action_prefix = "draft_"
    permission_policy_cls = FromConfig(
        "GEO_RDM_PACKAGE_PERMISSION_POLICY",
        default=GEOPackageRecordPermissionPolicy,
        import_string=True,
    )
