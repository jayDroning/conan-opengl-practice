cmake_minimum_required(VERSION 3.15)
project(conan-opengl-practice CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 🔽 Include all Conan-generated packages
include(${CMAKE_BINARY_DIR}/conandeps_legacy.cmake)

add_executable(conan-opengl-practice
        src/conan-opengl-practice.cpp
        src/main.cpp
        )

# Link Conan packages
target_link_libraries(conan-opengl-practice
        PRIVATE
        glfw
        glm::glm
        opengl::opengl
        )

# Optional: Set C++ standard explicitly
target_compile_features(conan-opengl-practice PRIVATE cxx_std_17)

install(TARGETS conan-opengl-practice DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
