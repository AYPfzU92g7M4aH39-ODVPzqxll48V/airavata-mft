# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scp/SCPStorageService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from airavata_mft_sdk.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from airavata_mft_sdk.google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from airavata_mft_sdk.scp import SCPStorage_pb2 as scp_dot_SCPStorage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bscp/SCPStorageService.proto\x12,org.apache.airavata.mft.resource.service.scp\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x14scp/SCPStorage.proto2\xa3\x07\n\x11SCPStorageService\x12\xcb\x01\n\x0elistSCPStorage\x12I.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageListRequest\x1aJ.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageListResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1.0/resource/scp/storage\x12\xbd\x01\n\rgetSCPStorage\x12H.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageGetRequest\x1a>.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorage\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1.0/resource/scp/storage\x12\xc3\x01\n\x10\x63reateSCPStorage\x12K.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageCreateRequest\x1a>.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorage\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/v1.0/resource/scp/storage\x12\x9b\x01\n\x10updateSCPStorage\x12K.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageUpdateRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/v1.0/resource/scp/storage\x12\x9b\x01\n\x10\x64\x65leteSCPStorage\x12K.org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageDeleteRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1.0/resource/scp/storageB\x02P\x01\x62\x06proto3')



_SCPSTORAGESERVICE = DESCRIPTOR.services_by_name['SCPStorageService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _SCPSTORAGESERVICE.methods_by_name['listSCPStorage']._options = None
  _SCPSTORAGESERVICE.methods_by_name['listSCPStorage']._serialized_options = b'\202\323\344\223\002\034\022\032/v1.0/resource/scp/storage'
  _SCPSTORAGESERVICE.methods_by_name['getSCPStorage']._options = None
  _SCPSTORAGESERVICE.methods_by_name['getSCPStorage']._serialized_options = b'\202\323\344\223\002\034\022\032/v1.0/resource/scp/storage'
  _SCPSTORAGESERVICE.methods_by_name['createSCPStorage']._options = None
  _SCPSTORAGESERVICE.methods_by_name['createSCPStorage']._serialized_options = b'\202\323\344\223\002\034\"\032/v1.0/resource/scp/storage'
  _SCPSTORAGESERVICE.methods_by_name['updateSCPStorage']._options = None
  _SCPSTORAGESERVICE.methods_by_name['updateSCPStorage']._serialized_options = b'\202\323\344\223\002\034\032\032/v1.0/resource/scp/storage'
  _SCPSTORAGESERVICE.methods_by_name['deleteSCPStorage']._options = None
  _SCPSTORAGESERVICE.methods_by_name['deleteSCPStorage']._serialized_options = b'\202\323\344\223\002\034*\032/v1.0/resource/scp/storage'
  _SCPSTORAGESERVICE._serialized_start=159
  _SCPSTORAGESERVICE._serialized_end=1090
# @@protoc_insertion_point(module_scope)