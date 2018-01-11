from conans import ConanFile, tools

class GslliteConan(ConanFile):
    name = "string-view-lite"
    version = "0.2.0"
    license = "MIT"
    url = "https://github.com/martinmoene/string-view-lite"
    description = "string_view lite - A single-file header-only version of a C++17-like string_view for C++98, C++11 and later"

    def source(self):
        self.run("git clone https://github.com/martinmoene/string-view-lite.git")
        self.run("cd string-view-lite && git checkout v0.2.0")

    def package(self):
        self.copy(pattern="string_view.hpp", src="string-view-lite/include/nonstd", dst="include", keep_path=False)