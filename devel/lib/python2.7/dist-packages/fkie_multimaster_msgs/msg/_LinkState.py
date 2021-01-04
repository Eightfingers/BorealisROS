# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fkie_multimaster_msgs/LinkState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class LinkState(genpy.Message):
  _md5sum = "fd2554dabc9a5d69f4842dd42dd3e0f3"
  _type = "fkie_multimaster_msgs/LinkState"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string destination
float32 quality
# The timestamp of the last received heartbeat message
time last_heartbeat
"""
  __slots__ = ['destination','quality','last_heartbeat']
  _slot_types = ['string','float32','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       destination,quality,last_heartbeat

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LinkState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.destination is None:
        self.destination = ''
      if self.quality is None:
        self.quality = 0.
      if self.last_heartbeat is None:
        self.last_heartbeat = genpy.Time()
    else:
      self.destination = ''
      self.quality = 0.
      self.last_heartbeat = genpy.Time()

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
      _x = self.destination
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f2I().pack(_x.quality, _x.last_heartbeat.secs, _x.last_heartbeat.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.last_heartbeat is None:
        self.last_heartbeat = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.destination = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.destination = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.quality, _x.last_heartbeat.secs, _x.last_heartbeat.nsecs,) = _get_struct_f2I().unpack(str[start:end])
      self.last_heartbeat.canon()
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
      _x = self.destination
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f2I().pack(_x.quality, _x.last_heartbeat.secs, _x.last_heartbeat.nsecs))
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
      if self.last_heartbeat is None:
        self.last_heartbeat = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.destination = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.destination = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.quality, _x.last_heartbeat.secs, _x.last_heartbeat.nsecs,) = _get_struct_f2I().unpack(str[start:end])
      self.last_heartbeat.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f2I = None
def _get_struct_f2I():
    global _struct_f2I
    if _struct_f2I is None:
        _struct_f2I = struct.Struct("<f2I")
    return _struct_f2I
