# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Geo Secretariat.
#
# geo-rdm-records is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""GEO Knowledge Hub records module"""

from .ext import GEORDMRecords
from .version import __version__

__all__ = ("__version__", "GEORDMRecords")
