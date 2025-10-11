#include <iostream>

#include "utils.hpp"
#include "other.hpp"

int main() {
    int sum1 = util::add(3, 4);
    int sum2 = get_second_sum();

    std::cout << "sum_1=" << sum1 << '\n';
    std::cout << "sum_2=" << sum2 << '\n';
    return 0;
}
