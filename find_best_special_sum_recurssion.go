/*
Find best special sum
Input
First line contains an integer 
 as input. Next line contains 
 space separated integers denoting the elements of the array 
.
Output
In the output you have to print an integer that denotes the maximum special sum

Sample Inputs

Input	Output
5
1 3 1 2 5

8
10
2 1 3 9 2 4 -10 -9 1 3
9

Sample Input
6
-3 2 3 -4 3 1
Sample Output
3

Explanation
Let us calculate the special value for each index :

For index 1: (A[1] + A[2]+A3]) + (A[4] + A[5] + A[6]) = 2
For index 2: A[2] + A[3] + A[4] = 1
For index 3: A[3] + A[4] + A[5] = 2
For index 4: A[4] + A[5] + A[6] = 0
For index 5: A[5] = 3
For index 6: A[6] = 1

*/

// Write your code here
package main
import "fmt"

func main(){
    var input [] int
    var temp int
    var max,sum,len int = 0,0,0
    fmt.Scanf("%d",&len)
    for i:=0;i<len;i++{
        fmt.Scanf("%d",&temp)
        input = append(input,temp)
    }
    for i:=0;i<len;i++{
        sum =find_max_sum(input[i:])
        if max < sum{
            max = sum
        }
    }
    fmt.Println(max)
}
func find_max_sum(A []int) int{ 
    var sum int = 0
    var n int
    n = len(A)
    sum = 0
    if n >=3 && n < 6{
        sum = A[0] + A[1] + A[2]
        return sum
    }else if n < 3{
        return A[0]
    }else if n >= 6{
        sum = A[0] + A[1] + A[2]
        sum = sum + find_max_sum(A[3:])
    }
return 0
}
