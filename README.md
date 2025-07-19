# conan-opengl-practice

🚀 A minimal modern OpenGL project using GLFW, GLM, and Conan 2 on C++17.  
🛠️ Cross-platform, CMake-based, and ready to build!

---

## Dependencies

This project uses the following libraries (installed via Conan 2):

- GLFW — window and context creation
- GLM — math library
- OpenGL (system) — provided by your GPU driver

---

## Requirements

- Conan 2 (install with `pip install conan`)
- CMake 3.15 or newer
- A C++17 compiler (tested with GCC 14.2 / MinGW)

---

## Project Structure

cpp-opengl-practice/
├── src/
│   └── main.cpp
├── CMakeLists.txt
├── conanfile.py
└── build/           # Created after Conan + CMake configure

---

## Building the Project

### 1. Install and configure dependencies via Conan

```bash
conan install . --build=missing [see Appendix A]
```

```bash
cmake -S . -B build -G [see Appendix A]
```

[Follow the link for Appendix A](#appendix-a---choosing-your-compiler)

### 2. Build the project

```bash
cmake --build build
```

### 3. Run the executable

```bash
./build/conan-opengl-practice
```

---

## Appendix A - Choosing your compiler

### Detect your compiler

```bash
conan profile detect --force
```

If you see from output the following line in config:

```bash
compiler=msvc
```

[Then follow the MSVC section](#appendix-b---msvc)

Otherwise if you see something else like:

```bash
compiler=gcc
```

- If you do have Ninja - [follow the Ninja section](#appendix-d---ninja)
- Otherwise - [follow the GCC with make section](#appendix-c---gcc-with-make-not-ninja)

[Then follow the GCC section](#appendix-c---gcc-with-make-not-ninja)

## Appendix B - MSVC

### Step 1. Install dependencies

If you're using Visual Studio and want to build with MSVC:

```bash
conan install . --build=missing \
  -c tools.cmake.cmaketoolchain:generator="Visual Studio 17 2022" \
  -s compiler=msvc -s compiler.version=193 \
  -s compiler.runtime=dynamic -s arch=x86_64
```

### Step 2. Configure dependencies

```bash
cmake -S . -B build -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake
```

[Then follow the next instructions](#2-build-the-project)

## Appendix C - GCC with Make (not Ninja)

### Step 1. Install dependencies

If you don’t have Ninja, use MinGW Makefiles:

```bash
conan install . --build=missing \
  -c tools.cmake.cmaketoolchain:generator="MinGW Makefiles" \
  -s compiler=gcc -s compiler.version=14 \
  -s compiler.libcxx=libstdc++11 -s arch=x86_64
```

### Step 2. Configure dependencies

```bash
cmake -S . -B build -G "MinGW Makefiles" -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake
```

[Then follow the next instructions](#2-build-the-project)

## Appendix D - Ninja

### Step 1. Install dependencies

```bash
conan install . --build=missing \
  -c tools.cmake.cmaketoolchain:generator="Ninja"
```

### Step 2. Configure dependencies

```bash
cmake -S . -B build -G Ninja -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake
```

[Then follow the next instructions](#2-build-the-project)

## Notes

- If you see `conandeps_legacy.cmake`, that's normal: some Conan packages still use legacy targets like `glfw` instead of `glfw::glfw`.
- If using MSYS2/MinGW, make sure your compiler and `mingw32-make` are in PATH.

---

## License

This project is licensed under the [MIT License](LICENSE).