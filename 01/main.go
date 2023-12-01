package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func f(d []string, N []string) {
	s := 0
	for _, l := range d {
		var S strings.Builder
		for i := 0; i < len(l); i++ {
			if l[i] >= '0' && l[i] <= '9' {
				S.WriteByte(l[i])
			}
			for j, n := range N {
				if strings.HasPrefix(l[i:], n) {
					S.WriteString(strconv.Itoa(j + 1))
				}
			}
		}
		val, _ := strconv.Atoi(string(S.String()[0]) + string(S.String()[len(S.String())-1]))
		s += val
	}
	fmt.Println(s)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var d []string

	for scanner.Scan() {
		d = append(d, scanner.Text())
	}

	f(d, []string{})
	f(d, []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"})
}
