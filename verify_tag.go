/*
tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel.
Determine if the tag is valid or not.
Sample Input
12X345-67
Sample Output
invalid
*/
package main
import (
    "fmt"
    "regexp"
    "os"
    )

func main(){
    var input string
    var sum,i int
    fmt.Scanf("%s",&input)
    case_pattern,_:= regexp.Compile("![aeiou]")
    digit_pattern,_:= regexp.Compile("[0-9]")
    for i=0;i< len(input);i++{
        sum=0 
        match1:= case_pattern.MatchString(string(input[i]))
        match2:= digit_pattern.MatchString(string(input[i]))
        if match1 == true{
                fmt.Println("invalid")
                os.Exit(1)
        }
        if match2 == true && digit_pattern.MatchString(string(input[i+1])){
            sum = int(input[i] - '0' + input[i+1] - '0')
            sum = sum %2
            if sum != 0{
                fmt.Printf("invalid")
                os.Exit(0)
            }
        }
    }
    fmt.Println("valid")
}
