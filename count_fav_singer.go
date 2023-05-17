/*
Bob has a playlist of 
 songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob
Sample Input
5
1 1 2 2 4
Sample Output
2
*/

package main
import "fmt"
func main(){
    var fav,count int= 0,0
    var new_val,n,num int
    var favsinger map[int]int
    favsinger = make(map[int]int)
    fmt.Scanf("%d",&n)
    for i:=0; i<n;i++{
        fmt.Scanf("%d", &num)
        _,present := favsinger[num]
        if(present){
            new_val = favsinger[num] + 1
            favsinger[num] = new_val
        }else{
            favsinger[num] = 1
        }
    }
    for _,songs := range favsinger{
        if(songs>fav){
            fav=songs
            count=1
        } else if(songs == fav){
            count++
        }
    }
    fmt.Println(count)
}
