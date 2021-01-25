# CMakeList.txt
# lib_src/
# ----------------------------------------------------------
# history
# 25/01/2021 First quit operational version ....... E. Dumas
# ----------------------------------------------------------

# I prefer :
# export CMAKE_GENERATOR=Ninja
#   but it's only an option

cmake_minimum_required(VERSION 3.0)

# set the project name
project(EDS-CV-Lib VERSION 0.1)

# https://stackoverflow.com/questions/31162438/how-can-i-build-rust-code-with-a-c-qt-cmake-project

# Enable ExternalProject CMake module
include(ExternalProject)

# Set default ExternalProject root directory
set_directory_properties(PROPERTIES EP_PREFIX ${CMAKE_BINARY_DIR}/Rust)

# Add lib as a CMake target
ExternalProject_Add(
    eds_cv_lib_rust
    DOWNLOAD_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND cargo build COMMAND cargo build --release
    BINARY_DIR "${CMAKE_SOURCE_DIR}/"
    INSTALL_COMMAND ""
    LOG_BUILD ON)

add_subdirectory(img_op)

message(STATUS "eds_cv_lib_sources - C Files - " ${eds_cv_lib_sources})

add_library(eds_cv_lib SHARED ${eds_cv_lib_sources} )

# Create dependency of eds_cv_lib on rust_lib
add_dependencies(eds_cv_lib eds_cv_lib_rust)

# Specify Example's link libraries
target_link_libraries(eds_cv_lib
    debug "${CMAKE_SOURCE_DIR}/target/debug/libeds_cv_lib_rust.a"
    optimized "${CMAKE_SOURCE_DIR}/target/release/libeds_cv_lib_rust.a"
    # ws2_32 userenv advapi32
)


target_include_directories(eds_cv_lib PUBLIC
                          "${PROJECT_SOURCE_DIR}/"
                          )
install(TARGETS eds_cv_lib DESTINATION lib)

# end of file
