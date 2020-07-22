from   conans       import ConanFile, CMake
from   distutils.dir_util import copy_tree

class FastNoiseConan(ConanFile):
    name            = "FastNoise"
    version         = "0.4"
    description     = "Conan package for FastNoise."
    url             = "https://github.com/Auburns/FastNoise"
    license         = "MIT"
    settings        = "arch", "build_type", "compiler", "os"
    generators      = "cmake"
    options         = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "CMakeLists.txt"

    def source(self):
        self.run("git clone -b %s --depth 1 https://github.com/Auburns/FastNoise.git" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def collect_headers(self, include_folder):
        self.copy("*.h"  , dst="include", src=include_folder)
        self.copy("*.hpp", dst="include", src=include_folder)
        self.copy("*.inl", dst="include", src=include_folder)

    def package(self):
        self.copy("*.h", dst="include", src="FastNoise")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["FastNoise"]