# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftp/FTPStorageService.proto
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
from airavata_mft_sdk.ftp import FTPStorage_pb2 as ftp_dot_FTPStorage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66tp/FTPStorageService.proto\x12,org.apache.airavata.mft.resource.service.ftp\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x14\x66tp/FTPStorage.proto2\xa3\x07\n\x11\x46TPStorageService\x12\xcb\x01\n\x0elistFTPStorage\x12I.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageListRequest\x1aJ.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageListResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1.0/resource/ftp/storage\x12\xbd\x01\n\rgetFTPStorage\x12H.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageGetRequest\x1a>.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorage\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1.0/resource/ftp/storage\x12\xc3\x01\n\x10\x63reateFTPStorage\x12K.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageCreateRequest\x1a>.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorage\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/v1.0/resource/ftp/storage\x12\x9b\x01\n\x10updateFTPStorage\x12K.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageUpdateRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/v1.0/resource/ftp/storage\x12\x9b\x01\n\x10\x64\x65leteFTPStorage\x12K.org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorageDeleteRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1.0/resource/ftp/storageB\x02P\x01\x62\x06proto3')



_FTPSTORAGESERVICE = DESCRIPTOR.services_by_name['FTPStorageService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _FTPSTORAGESERVICE.methods_by_name['listFTPStorage']._options = None
  _FTPSTORAGESERVICE.methods_by_name['listFTPStorage']._serialized_options = b'\202\323\344\223\002\034\022\032/v1.0/resource/ftp/storage'
  _FTPSTORAGESERVICE.methods_by_name['getFTPStorage']._options = None
  _FTPSTORAGESERVICE.methods_by_name['getFTPStorage']._serialized_options = b'\202\323\344\223\002\034\022\032/v1.0/resource/ftp/storage'
  _FTPSTORAGESERVICE.methods_by_name['createFTPStorage']._options = None
  _FTPSTORAGESERVICE.methods_by_name['createFTPStorage']._serialized_options = b'\202\323\344\223\002\034\"\032/v1.0/resource/ftp/storage'
  _FTPSTORAGESERVICE.methods_by_name['updateFTPStorage']._options = None
  _FTPSTORAGESERVICE.methods_by_name['updateFTPStorage']._serialized_options = b'\202\323\344\223\002\034\032\032/v1.0/resource/ftp/storage'
  _FTPSTORAGESERVICE.methods_by_name['deleteFTPStorage']._options = None
  _FTPSTORAGESERVICE.methods_by_name['deleteFTPStorage']._serialized_options = b'\202\323\344\223\002\034*\032/v1.0/resource/ftp/storage'
  _FTPSTORAGESERVICE._serialized_start=159
  _FTPSTORAGESERVICE._serialized_end=1090
# @@protoc_insertion_point(module_scope)