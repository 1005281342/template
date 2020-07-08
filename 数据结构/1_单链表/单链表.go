package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const N = 100010

var (
	head = -1                // 记录头节点位置
	idx  = 0                 // 当前可使用点的下标（指针）
	e    = make([]int, N, N) // 值数组，初始化默认值为0
	ne   = make([]int, N, N) // 指针数组
)

func init() {
	// 数组元素初始化为-1, -1表示该点的指向的下一个节点为空
	for i := 0; i < N; i++ {
		ne[i] = -1
	}
}

// addToHead 将x插入到头节点
func addToHead(x int) {
	// 将x写入当前可用节点a
	e[idx] = x
	// 将当前节点a指向头节点，使节点a作为头节点
	ne[idx] = head
	// 记录头节点位置
	head = idx
	// 选择下一个可用节点
	idx++
}

// 将x插入到下标为k的点的后面
func add(k, x int) {
	// 将x的值写入当前可用的点a
	e[idx] = x
	// 使节点a指向节点k的下一节点
	ne[idx] = ne[k]
	// 使节点k的下一个节点指向节点a
	ne[k] = idx
	idx++
}

// 将下标为k的点的后面第一个元素移除
func remove(k int) {
	ne[k] = ne[ne[k]]
}

func ReadLine(reader *bufio.Reader) string {
	line, _ := reader.ReadString('\n')
	return strings.TrimRight(line, "\n")
}

func ReadInt(reader *bufio.Reader) int {
	num, _ := strconv.Atoi(ReadLine(reader))
	return num
}

func ReadArray(reader *bufio.Reader) []int {
	line := ReadLine(reader)
	strs := strings.Split(line, " ")
	nums := make([]int, len(strs))
	for i, s := range strs {
		nums[i], _ = strconv.Atoi(s)
	}
	return nums
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var m = ReadInt(reader)
	for i := 0; i < m; i++ {
		var (
			k int
			x int
		)
		var t = strings.Split(ReadLine(reader), " ")
		// 将x插入到头节点
		if t[0] == "H" {
			x, _ = strconv.Atoi(t[1])
			addToHead(x)
		} else if t[0] == "D" { // 移除第K个节点
			k, _ = strconv.Atoi(t[1])
			if k == 0 { // 移除头节点
				head = ne[head]
				continue
			}
			// remove 使移除下标为idx的下一个元素
			remove(k - 1)
		} else {
			k, _ = strconv.Atoi(t[1])
			x, _ = strconv.Atoi(t[2])
			add(k-1, x)
		}
	}

	var i = head
	for i != -1 {
		fmt.Println(e[i])
		i = ne[i]
	}
}

//IN:
//10
//H 9
//I 1 1
//D 1
//D 0
//H 6
//I 3 6
//I 4 5
//I 4 5
//I 3 4
//D 6
//OUT:
//6
//4
//6
//5
