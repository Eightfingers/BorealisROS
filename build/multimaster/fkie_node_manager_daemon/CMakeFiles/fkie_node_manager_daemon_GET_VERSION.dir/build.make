# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/apex-15/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/apex-15/catkin_ws/build

# Utility rule file for fkie_node_manager_daemon_GET_VERSION.

# Include the progress variables for this target.
include multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/progress.make

multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION: /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/VERSION
multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION: /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/DATE
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/apex-15/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generate version files"

/home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/VERSION:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/apex-15/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "create version file /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/VERSION"
	cd /home/apex-15/catkin_ws/src/multimaster/fkie_node_manager_daemon && bash -c "/usr/bin/git describe --tags --dirty --always > /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/VERSION"

/home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/DATE:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/apex-15/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "create date file /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/DATE"
	cd /home/apex-15/catkin_ws/src/multimaster/fkie_node_manager_daemon && bash -c "/usr/bin/git show -s --format=%ci > /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/DATE"

fkie_node_manager_daemon_GET_VERSION: multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION
fkie_node_manager_daemon_GET_VERSION: /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/VERSION
fkie_node_manager_daemon_GET_VERSION: /home/apex-15/catkin_ws/devel/share/fkie_node_manager_daemon/DATE
fkie_node_manager_daemon_GET_VERSION: multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/build.make

.PHONY : fkie_node_manager_daemon_GET_VERSION

# Rule to build all files generated by this target.
multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/build: fkie_node_manager_daemon_GET_VERSION

.PHONY : multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/build

multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/clean:
	cd /home/apex-15/catkin_ws/build/multimaster/fkie_node_manager_daemon && $(CMAKE_COMMAND) -P CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/cmake_clean.cmake
.PHONY : multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/clean

multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/depend:
	cd /home/apex-15/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/apex-15/catkin_ws/src /home/apex-15/catkin_ws/src/multimaster/fkie_node_manager_daemon /home/apex-15/catkin_ws/build /home/apex-15/catkin_ws/build/multimaster/fkie_node_manager_daemon /home/apex-15/catkin_ws/build/multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : multimaster/fkie_node_manager_daemon/CMakeFiles/fkie_node_manager_daemon_GET_VERSION.dir/depend

