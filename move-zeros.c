#include<stdio.h>
void moveZeroes(int* nums, int numsSize);
int main(){
  nums = [0, 1, 0 , 3, 12];
  moveZeros(nums, 5);
  return 0;
}

void moveZeroes(int* nums, int numsSize){
    int i,j;
    int non_zero_index = 0;
    for(i=0;i<numsSize;i++){
        if(nums[i] != 0){
            nums[non_zero_index++] = nums[i];
        }
    }
    for(i = non_zero_index++;i<numsSize;i++){
        nums[i] = 0;
    }
}
