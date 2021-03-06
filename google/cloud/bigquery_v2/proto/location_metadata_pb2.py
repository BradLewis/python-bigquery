# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery_v2/proto/location_metadata.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery_v2/proto/location_metadata.proto",
    package="google.cloud.bigquery.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.cloud.bigquery.v2B\025LocationMetadataProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigquery"
    ),
    serialized_pb=_b(
        '\n6google/cloud/bigquery_v2/proto/location_metadata.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto".\n\x10LocationMetadata\x12\x1a\n\x12legacy_location_id\x18\x01 \x01(\tBw\n\x1c\x63om.google.cloud.bigquery.v2B\x15LocationMetadataProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigqueryb\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_LOCATIONMETADATA = _descriptor.Descriptor(
    name="LocationMetadata",
    full_name="google.cloud.bigquery.v2.LocationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="legacy_location_id",
            full_name="google.cloud.bigquery.v2.LocationMetadata.legacy_location_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=114,
    serialized_end=160,
)

DESCRIPTOR.message_types_by_name["LocationMetadata"] = _LOCATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationMetadata = _reflection.GeneratedProtocolMessageType(
    "LocationMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LOCATIONMETADATA,
        __module__="google.cloud.bigquery_v2.proto.location_metadata_pb2",
        __doc__="""BigQuery-specific metadata about a location. This will be set on
  google.cloud.location.Location.metadata in Cloud Location API responses.
  
  
  Attributes:
      legacy_location_id:
          The legacy BigQuery location ID, e.g. ``EU`` for the ``europe``
          location. This is for any API consumers that need the legacy
          ``US`` and ``EU`` locations.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.v2.LocationMetadata)
    ),
)
_sym_db.RegisterMessage(LocationMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
