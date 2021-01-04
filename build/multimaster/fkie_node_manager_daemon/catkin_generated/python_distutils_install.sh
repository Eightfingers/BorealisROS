#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/apex-15/catkin_ws/src/multimaster/fkie_node_manager_daemon"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/apex-15/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/apex-15/catkin_ws/install/lib/python2.7/dist-packages:/home/apex-15/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/apex-15/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/apex-15/catkin_ws/src/multimaster/fkie_node_manager_daemon/setup.py" \
     \
    build --build-base "/home/apex-15/catkin_ws/build/multimaster/fkie_node_manager_daemon" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/apex-15/catkin_ws/install" --install-scripts="/home/apex-15/catkin_ws/install/bin"
