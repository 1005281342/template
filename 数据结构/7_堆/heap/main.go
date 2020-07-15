package main

import "fmt"

const N = 100010

var cnt = 5
var m = 3

var h = make([]int, N, N)

func down(u int) {
    var t = u
    if 2*u <= cnt && h[2*u] < h[t] {
        t = 2*u
    }
    if 2*u+1 <= cnt && h[2*u+1] < h[t] {
        t = 2*u+1
    }
    if t!=u{
        h[t], h[u] = h[u], h[t]
        down(t)
    }
}

func up(u int) {
    for u>>1 > 0 && (h[u] < h[u>>1]) {
        h[u], h[u>>1] = h[u>>1], h[u]
        u >>= 1
    }
}

func main() {
    var nums = []int{4, 5, 1, 2, 3}
    for i := 0; i<len(nums); i++ {
        h[i+1] = nums[i]
    }

    for i:=cnt/2; i>0; i-- {
        down(i)
    }

    for i:=0; i<m; i++ {
        fmt.Println(h[1])
        h[1] = h[cnt]
        cnt -= 1
        down(1)
    }
}