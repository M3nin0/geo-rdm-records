/*
 * This file is part of Geo Secretariat.
 * Copyright (C) 2022 GEO Secretariat.
 *
 * GEO-RDM-Records is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

import { createSearchAppInit } from "@js/invenio_search_ui";
import { CustomRecordResultsListItem } from "./components";

import {
  CommunitiesFacetsValues,
  CommunityBucketAggregationElement,
  CommunityCountComponent,
  CommunityEmptyResults,
  CommunityErrorComponent,
  CommunityRecordFacets,
  CommunityRecordResultsGridItem,
  CommunityRecordSearchAppLayout,
  CommunityRecordSearchBarElement,
} from "@js/invenio_communities/details_search/components";

import { CustomToggleVersion } from "./components";

createSearchAppInit({
  "BucketAggregation.element": CommunityBucketAggregationElement,
  "BucketAggregationValues.element": CommunitiesFacetsValues,
  "ResultsGrid.item": CommunityRecordResultsGridItem,
  "EmptyResults.element": CommunityEmptyResults,
  "ResultsList.item": CustomRecordResultsListItem,
  "SearchApp.facets": CommunityRecordFacets,
  "SearchApp.layout": CommunityRecordSearchAppLayout,
  "SearchBar.element": CommunityRecordSearchBarElement,
  "Count.element": CommunityCountComponent,
  "Error.element": CommunityErrorComponent,
  "SearchFilters.Toggle.element": CustomToggleVersion,
});
