// Generated by gencpp from file fkie_multimaster_msgs/TaskRequest.msg
// DO NOT EDIT!


#ifndef FKIE_MULTIMASTER_MSGS_MESSAGE_TASKREQUEST_H
#define FKIE_MULTIMASTER_MSGS_MESSAGE_TASKREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fkie_multimaster_msgs
{
template <class ContainerAllocator>
struct TaskRequest_
{
  typedef TaskRequest_<ContainerAllocator> Type;

  TaskRequest_()
    : node()  {
    }
  TaskRequest_(const ContainerAllocator& _alloc)
    : node(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _node_type;
  _node_type node;





  typedef boost::shared_ptr< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> const> ConstPtr;

}; // struct TaskRequest_

typedef ::fkie_multimaster_msgs::TaskRequest_<std::allocator<void> > TaskRequest;

typedef boost::shared_ptr< ::fkie_multimaster_msgs::TaskRequest > TaskRequestPtr;
typedef boost::shared_ptr< ::fkie_multimaster_msgs::TaskRequest const> TaskRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator1> & lhs, const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator2> & rhs)
{
  return lhs.node == rhs.node;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator1> & lhs, const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace fkie_multimaster_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a94c40e70a4b82863e6e52ec16732447";
  }

  static const char* value(const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa94c40e70a4b8286ULL;
  static const uint64_t static_value2 = 0x3e6e52ec16732447ULL;
};

template<class ContainerAllocator>
struct DataType< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fkie_multimaster_msgs/TaskRequest";
  }

  static const char* value(const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string node\n"
;
  }

  static const char* value(const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.node);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TaskRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fkie_multimaster_msgs::TaskRequest_<ContainerAllocator>& v)
  {
    s << indent << "node: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.node);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FKIE_MULTIMASTER_MSGS_MESSAGE_TASKREQUEST_H
