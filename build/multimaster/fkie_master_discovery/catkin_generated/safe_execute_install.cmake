execute_process(COMMAND "/home/apex-15/catkin_ws/build/multimaster/fkie_master_discovery/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/apex-15/catkin_ws/build/multimaster/fkie_master_discovery/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
