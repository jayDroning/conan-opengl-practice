#include "conan-opengl-practice.h"
#include <vector>
#include <string>

int main() {
    conan_opengl_practice();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    conan_opengl_practice_print_vector(vec);
}
