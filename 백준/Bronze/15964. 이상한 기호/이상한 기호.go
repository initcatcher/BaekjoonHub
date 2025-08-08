package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	result := (a + b) * (a - b)
	fmt.Println(result)
}
