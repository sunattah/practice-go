package main 


import(
	"fmt"
	"strings"
)
func main() {
	text := "through"
	wordleter := strings.ToUpper(string(text[0])) + strings.ToLower(string(text[1:]))
	fmt.Println(wordleter)
}
