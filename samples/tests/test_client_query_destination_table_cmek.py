# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .. import client_query_destination_table_cmek


def test_client_query_destination_table_cmek(capsys, random_table_id, kms_key_name):

    client_query_destination_table_cmek.client_query_destination_table_cmek(
        random_table_id, kms_key_name
    )
    out, err = capsys.readouterr()
    assert "The destination table is written using the encryption configuration" in out
