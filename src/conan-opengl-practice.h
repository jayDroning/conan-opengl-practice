#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define CONAN_OPENGL_PRACTICE_EXPORT __declspec(dllexport)
#else
  #define CONAN_OPENGL_PRACTICE_EXPORT
#endif

CONAN_OPENGL_PRACTICE_EXPORT void conan_opengl_practice();
CONAN_OPENGL_PRACTICE_EXPORT void conan_opengl_practice_print_vector(const std::vector<std::string> &strings);
