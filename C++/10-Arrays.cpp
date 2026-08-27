#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    
    int nums[10];
    nums[0] = 100;
    nums[1] = 400;
    nums[2] = 300;
    nums[3] = 200;
    nums[4] = 80;
    nums[5] = 70;
    nums[6] = 10;
    nums[7] = 99;
    nums[8] = 102;
    nums[9] = 101;

    int nums2[] = {1, 3, 4, 5, 6, 7, 11, 12, 17};

    // PERCORRENDO UM ARRAY COM FOR
    for(int i = 0; i<9; i++) {
        cout << i << " - " << nums2[i] << endl;
    }

    system("pause");
    return 0;
}