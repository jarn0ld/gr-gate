INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GATE gate)

FIND_PATH(
    GATE_INCLUDE_DIRS
    NAMES gate/api.h
    HINTS $ENV{GATE_DIR}/include
        ${PC_GATE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GATE_LIBRARIES
    NAMES gnuradio-gate
    HINTS $ENV{GATE_DIR}/lib
        ${PC_GATE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GATE DEFAULT_MSG GATE_LIBRARIES GATE_INCLUDE_DIRS)
MARK_AS_ADVANCED(GATE_LIBRARIES GATE_INCLUDE_DIRS)

