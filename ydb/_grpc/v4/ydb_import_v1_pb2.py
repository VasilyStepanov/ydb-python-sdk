# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_import_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_import_pb2 as protos_dot_ydb__import__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13ydb_import_v1.proto\x12\rYdb.Import.V1\x1a\x17protos/ydb_import.proto2\xaf\x01\n\rImportService\x12Q\n\x0cImportFromS3\x12\x1f.Ydb.Import.ImportFromS3Request\x1a .Ydb.Import.ImportFromS3Response\x12K\n\nImportData\x12\x1d.Ydb.Import.ImportDataRequest\x1a\x1e.Ydb.Import.ImportDataResponseBL\n\x13tech.ydb.import_.v1Z5github.com/ydb-platform/ydb-go-genproto/Ydb_Import_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ydb_import_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023tech.ydb.import_.v1Z5github.com/ydb-platform/ydb-go-genproto/Ydb_Import_V1'
  _IMPORTSERVICE._serialized_start=64
  _IMPORTSERVICE._serialized_end=239
# @@protoc_insertion_point(module_scope)