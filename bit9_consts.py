# File: bit9_consts.py
# Copyright (c) 2016-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
ERROR_PARSING_JSON = "Error parsing the response as JSON"
BIT9_JSON_BASE_URL = "base_url"
BIT9_JSON_API_TOKEN = "api_token"
BIT9_JSON_DESCRIPTION = "comment"
BIT9_JSON_UNBLOCK_STATE = "file_state"

VERIFY_CERT = "verify_server_cert"
FILE_CATALOG_ENDPOINT = "/filecatalog"
FILE_RULE_ENDPOINT = "/fileRule"
FILE_UPLOAD_ENDPOINT = "/fileUpload"
CAT_ID_DATA = "fileCatalogId:%s"
APPEND_HASHES = "%s:%s"
LISTDECISION_MAP = {"white": "2", "black": "3"}
APPEND_NOT_POLICY = "%s%s"
B9FID = "id"
DECISION_MAP = {"local_approval": "localState", "global_approval": "fileState"}
BIT9_API_URI = "/api/bit9platform/v1"
BIT9_LIST_FILES_SUCC = "Number of files returned: {0}"
BIT9_GET_FILE_SUCC = "Successfully added file to vault. Vault ID: {0}"

BIT9_ERR_FROM_SERVER = "API failed, Status code: {status}, Detail: {detail}"
BIT9_ERR_JSON_PARSE = "Unable to parse reply as a Json, raw string reply: '{raw_text}'"
BIT9_ERR_API_UNSUPPORTED_METHOD = "Unsupported method"
BIT9_ERR_SERVER_CONNECTION = "Connection failed"

BIT9_FILE_STATE_UNAPPROVED = "1"
BIT9_FILE_STATE_APPROVED = "2"
BIT9_FILE_STATE_BANNED = "3"

BIT9_UNBLOCK_STATE_MAP = {"approved": BIT9_FILE_STATE_APPROVED, "unapproved": BIT9_FILE_STATE_UNAPPROVED}
BIT9_DEFAULT_UNBLOCK_STATE = "unapproved"
BIT9_ADDED_BY_PHANTOM = "Added by Phantom Installation ID: {0}"

BIT9_INVALID_INT = "Please provide a valid integer value in the {param}"
BIT9_ERR_NEGATIVE_INT_PARAM = "Please provide a valid non-negative integer value in the {param}"
BIT9_ERR_INVALID_PARAM = "Please provide a non-zero positive integer in the {param}"

ERR_CODE_UNAVAILABLE = "Error code unavailable"
ERR_MSG_UNAVAILABLE = "Unknown error occurred. Please check the action parameters."

BIT9_DEFAULT_TIMEOUT = 30
