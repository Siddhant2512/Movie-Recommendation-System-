# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/CameraInput.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/CameraInput.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!streamlit/proto/CameraInput.proto\"Y\n\x0b\x43\x61meraInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0c\n\x04help\x18\x03 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x04 \x01(\t\x12\x10\n\x08\x64isabled\x18\x05 \x01(\x08\x62\x06proto3'
)




_CAMERAINPUT = _descriptor.Descriptor(
  name='CameraInput',
  full_name='CameraInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CameraInput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='CameraInput.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='help', full_name='CameraInput.help', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='form_id', full_name='CameraInput.form_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='CameraInput.disabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['CameraInput'] = _CAMERAINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraInput = _reflection.GeneratedProtocolMessageType('CameraInput', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAINPUT,
  '__module__' : 'streamlit.proto.CameraInput_pb2'
  # @@protoc_insertion_point(class_scope:CameraInput)
  })
_sym_db.RegisterMessage(CameraInput)


# @@protoc_insertion_point(module_scope)
