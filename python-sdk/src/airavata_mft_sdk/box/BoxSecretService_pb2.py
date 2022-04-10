# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: box/BoxSecretService.proto
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
from airavata_mft_sdk.box import BoxCredential_pb2 as box_dot_BoxCredential__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x62ox/BoxSecretService.proto\x12.org.apache.airavata.mft.credential.service.box\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17\x62ox/BoxCredential.proto2\xfe\x04\n\x10\x42oxSecretService\x12\xa4\x01\n\x0cgetBoxSecret\x12\x41.org.apache.airavata.mft.credential.stubs.box.BoxSecretGetRequest\x1a\x37.org.apache.airavata.mft.credential.stubs.box.BoxSecret\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1.0/secret/box\x12\xaa\x01\n\x0f\x63reateBoxSecret\x12\x44.org.apache.airavata.mft.credential.stubs.box.BoxSecretCreateRequest\x1a\x37.org.apache.airavata.mft.credential.stubs.box.BoxSecret\"\x18\x82\xd3\xe4\x93\x02\x12\"\x10/v1.0/secret/box\x12\x89\x01\n\x0fupdateBoxSecret\x12\x44.org.apache.airavata.mft.credential.stubs.box.BoxSecretUpdateRequest\x1a\x16.google.protobuf.Empty\"\x18\x82\xd3\xe4\x93\x02\x12\x1a\x10/v1.0/secret/box\x12\x89\x01\n\x0f\x64\x65leteBoxSecret\x12\x44.org.apache.airavata.mft.credential.stubs.box.BoxSecretDeleteRequest\x1a\x16.google.protobuf.Empty\"\x18\x82\xd3\xe4\x93\x02\x12*\x10/v1.0/secret/boxB\x02P\x01\x62\x06proto3')



_BOXSECRETSERVICE = DESCRIPTOR.services_by_name['BoxSecretService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _BOXSECRETSERVICE.methods_by_name['getBoxSecret']._options = None
  _BOXSECRETSERVICE.methods_by_name['getBoxSecret']._serialized_options = b'\202\323\344\223\002\022\022\020/v1.0/secret/box'
  _BOXSECRETSERVICE.methods_by_name['createBoxSecret']._options = None
  _BOXSECRETSERVICE.methods_by_name['createBoxSecret']._serialized_options = b'\202\323\344\223\002\022\"\020/v1.0/secret/box'
  _BOXSECRETSERVICE.methods_by_name['updateBoxSecret']._options = None
  _BOXSECRETSERVICE.methods_by_name['updateBoxSecret']._serialized_options = b'\202\323\344\223\002\022\032\020/v1.0/secret/box'
  _BOXSECRETSERVICE.methods_by_name['deleteBoxSecret']._options = None
  _BOXSECRETSERVICE.methods_by_name['deleteBoxSecret']._serialized_options = b'\202\323\344\223\002\022*\020/v1.0/secret/box'
  _BOXSECRETSERVICE._serialized_start=163
  _BOXSECRETSERVICE._serialized_end=801
# @@protoc_insertion_point(module_scope)