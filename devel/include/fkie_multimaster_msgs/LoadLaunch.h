// Generated by gencpp from file fkie_multimaster_msgs/LoadLaunch.msg
// DO NOT EDIT!


#ifndef FKIE_MULTIMASTER_MSGS_MESSAGE_LOADLAUNCH_H
#define FKIE_MULTIMASTER_MSGS_MESSAGE_LOADLAUNCH_H

#include <ros/service_traits.h>


#include <fkie_multimaster_msgs/LoadLaunchRequest.h>
#include <fkie_multimaster_msgs/LoadLaunchResponse.h>


namespace fkie_multimaster_msgs
{

struct LoadLaunch
{

typedef LoadLaunchRequest Request;
typedef LoadLaunchResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct LoadLaunch
} // namespace fkie_multimaster_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::fkie_multimaster_msgs::LoadLaunch > {
  static const char* value()
  {
    return "1d00cd540af97efeb6b1589112fab63e";
  }

  static const char* value(const ::fkie_multimaster_msgs::LoadLaunch&) { return value(); }
};

template<>
struct DataType< ::fkie_multimaster_msgs::LoadLaunch > {
  static const char* value()
  {
    return "fkie_multimaster_msgs/LoadLaunch";
  }

  static const char* value(const ::fkie_multimaster_msgs::LoadLaunch&) { return value(); }
};


// service_traits::MD5Sum< ::fkie_multimaster_msgs::LoadLaunchRequest> should match
// service_traits::MD5Sum< ::fkie_multimaster_msgs::LoadLaunch >
template<>
struct MD5Sum< ::fkie_multimaster_msgs::LoadLaunchRequest>
{
  static const char* value()
  {
    return MD5Sum< ::fkie_multimaster_msgs::LoadLaunch >::value();
  }
  static const char* value(const ::fkie_multimaster_msgs::LoadLaunchRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::fkie_multimaster_msgs::LoadLaunchRequest> should match
// service_traits::DataType< ::fkie_multimaster_msgs::LoadLaunch >
template<>
struct DataType< ::fkie_multimaster_msgs::LoadLaunchRequest>
{
  static const char* value()
  {
    return DataType< ::fkie_multimaster_msgs::LoadLaunch >::value();
  }
  static const char* value(const ::fkie_multimaster_msgs::LoadLaunchRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::fkie_multimaster_msgs::LoadLaunchResponse> should match
// service_traits::MD5Sum< ::fkie_multimaster_msgs::LoadLaunch >
template<>
struct MD5Sum< ::fkie_multimaster_msgs::LoadLaunchResponse>
{
  static const char* value()
  {
    return MD5Sum< ::fkie_multimaster_msgs::LoadLaunch >::value();
  }
  static const char* value(const ::fkie_multimaster_msgs::LoadLaunchResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::fkie_multimaster_msgs::LoadLaunchResponse> should match
// service_traits::DataType< ::fkie_multimaster_msgs::LoadLaunch >
template<>
struct DataType< ::fkie_multimaster_msgs::LoadLaunchResponse>
{
  static const char* value()
  {
    return DataType< ::fkie_multimaster_msgs::LoadLaunch >::value();
  }
  static const char* value(const ::fkie_multimaster_msgs::LoadLaunchResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // FKIE_MULTIMASTER_MSGS_MESSAGE_LOADLAUNCH_H
