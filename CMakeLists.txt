cmake_minimum_required(VERSION 3.5)
project(FastNoise)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

file(GLOB_RECURSE SRC "."
    "*.h"
    "*.cpp"
)
add_library(FastNoise STATIC ${SRC})