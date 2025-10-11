#ifndef UTILS_HPP
#define UTILS_HPP

namespace util {

// Intentional ODR issue: non-inline function definitions in a header
int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

}  // namespace util

#endif  // UTILS_HPP
