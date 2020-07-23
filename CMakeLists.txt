cmake_minimum_required(VERSION 3.5)
project(FastNoise)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(FastNoise
    "FastNoise/FastNoise.h"
    "FastNoise/FastNoise.cpp"
)