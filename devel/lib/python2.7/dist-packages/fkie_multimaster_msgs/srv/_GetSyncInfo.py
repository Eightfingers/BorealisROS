# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fkie_multimaster_msgs/GetSyncInfoRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetSyncInfoRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "fkie_multimaster_msgs/GetSyncInfoRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetSyncInfoRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fkie_multimaster_msgs/GetSyncInfoResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import fkie_multimaster_msgs.msg

class GetSyncInfoResponse(genpy.Message):
  _md5sum = "d5261ec56e202860a07fb47b41e1b2a8"
  _type = "fkie_multimaster_msgs/GetSyncInfoResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """fkie_multimaster_msgs/SyncMasterInfo[] hosts

================================================================================
MSG: fkie_multimaster_msgs/SyncMasterInfo
string masteruri
string[] nodes
fkie_multimaster_msgs/SyncTopicInfo[] publisher
fkie_multimaster_msgs/SyncTopicInfo[] subscriber
fkie_multimaster_msgs/SyncServiceInfo[] services
================================================================================
MSG: fkie_multimaster_msgs/SyncTopicInfo
string topic
string node
string nodeuri
================================================================================
MSG: fkie_multimaster_msgs/SyncServiceInfo
string service
string serviceuri
string node
string nodeuri"""
  __slots__ = ['hosts']
  _slot_types = ['fkie_multimaster_msgs/SyncMasterInfo[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       hosts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetSyncInfoResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.hosts is None:
        self.hosts = []
    else:
      self.hosts = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.hosts)
      buff.write(_struct_I.pack(length))
      for val1 in self.hosts:
        _x = val1.masteruri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.nodes)
        buff.write(_struct_I.pack(length))
        for val2 in val1.nodes:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.publisher)
        buff.write(_struct_I.pack(length))
        for val2 in val1.publisher:
          _x = val2.topic
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.subscriber)
        buff.write(_struct_I.pack(length))
        for val2 in val1.subscriber:
          _x = val2.topic
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.services)
        buff.write(_struct_I.pack(length))
        for val2 in val1.services:
          _x = val2.service
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.serviceuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.hosts is None:
        self.hosts = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hosts = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncMasterInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.masteruri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.masteruri = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.nodes = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.nodes.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.publisher = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncTopicInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.topic = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.topic = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.publisher.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.subscriber = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncTopicInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.topic = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.topic = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.subscriber.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.services = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncServiceInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.service = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.service = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.serviceuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.serviceuri = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.services.append(val2)
        self.hosts.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.hosts)
      buff.write(_struct_I.pack(length))
      for val1 in self.hosts:
        _x = val1.masteruri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.nodes)
        buff.write(_struct_I.pack(length))
        for val2 in val1.nodes:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.publisher)
        buff.write(_struct_I.pack(length))
        for val2 in val1.publisher:
          _x = val2.topic
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.subscriber)
        buff.write(_struct_I.pack(length))
        for val2 in val1.subscriber:
          _x = val2.topic
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.services)
        buff.write(_struct_I.pack(length))
        for val2 in val1.services:
          _x = val2.service
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.serviceuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.nodeuri
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.hosts is None:
        self.hosts = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hosts = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncMasterInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.masteruri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.masteruri = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.nodes = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.nodes.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.publisher = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncTopicInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.topic = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.topic = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.publisher.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.subscriber = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncTopicInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.topic = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.topic = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.subscriber.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.services = []
        for i in range(0, length):
          val2 = fkie_multimaster_msgs.msg.SyncServiceInfo()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.service = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.service = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.serviceuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.serviceuri = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.node = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.nodeuri = str[start:end]
          val1.services.append(val2)
        self.hosts.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class GetSyncInfo(object):
  _type          = 'fkie_multimaster_msgs/GetSyncInfo'
  _md5sum = 'd5261ec56e202860a07fb47b41e1b2a8'
  _request_class  = GetSyncInfoRequest
  _response_class = GetSyncInfoResponse