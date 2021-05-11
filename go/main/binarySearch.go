package main

import "fmt"

func main() {
	items := []int{1, 2, 9, 20, 31, 45, 63, 70, 100}
	fmt.Println(binarySearch(items, 63))
}

func binarySearch(sortedList []int, lookingFor int) int {
	var lo int = 0
	var hi int = len(sortedList) - 1

	for lo <= hi {
		var mid int = (lo + hi) / 2

		if sortedList[mid] == lookingFor {
			return mid
		} else if sortedList[mid] > lookingFor {
			// We want to use the left half of our list
			hi = mid - 1
		} else {
			// We want to use the right half of our list
			lo = mid + 1
		}
	}

	// If we get here we tried to look at an invalid sub-list
	// which means the number isn't in our list.
	return -1
}
