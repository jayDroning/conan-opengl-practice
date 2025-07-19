from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class conan_opengl_practiceRecipe(ConanFile):
    name = "conan-opengl-practice"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "MIT License"
    author = "Leonid Dorokhov"
    url = "https://github.com/jayDroning/conan-opengl-practice.git"
    description = "The unique approach in opengl application development"
    topics = ("cpp", "opengl", "gamedev", "game development", "graphics", "practice")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    default_options = {
        "glfw/*:shared": False,
        "glfw/*:vulkan_static": False,
    }
    
    def layout(self):
        self.folders.build = "build"
        self.folders.source = "."
        self.folders.generators = "build"

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def requirements(self):
        self.requires("glfw/3.3.8")
        self.requires("glm/0.9.9.8")
        self.requires("opengl/system")

    

    
