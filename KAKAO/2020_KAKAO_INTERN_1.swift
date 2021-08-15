
import Foundation

let keypad = ["1": (0, 0), "2": (0, 1), "3": (0, 2),
              "4": (1, 0), "5": (1, 1), "6": (1, 2),
              "7": (2, 0), "8": (2, 1), "9": (2, 2),
              "*": (3, 0), "0": (3, 1), "#": (3, 2)
             ]

func distance(_ from: String, _ to: String) -> Int {
    let positionX = keypad[from]!
    let positionY = keypad[to]!
    return abs(positionX.0 - positionY.0) + abs(positionX.1 - positionY.1)
}

func solution(_ numbers:[Int], _ hand:String) -> String {
    var leftHand = "*"
    var rightHand = "#"
    var result = ""
    for number in numbers {
        
        if [1, 4, 7].contains(number) {
            result.append("L")
            leftHand = String(number)
            continue
        }
        
        if [3, 6, 9].contains(number) {
            result.append("R")
            rightHand = String(number)
            continue
        }
        
        let subtracted = distance(leftHand, String(number)) - distance(rightHand, String(number))
        
        if subtracted < 0 {
            result.append("L")
            leftHand = String(number)
        } else if subtracted > 0 {
            result.append("R")
            rightHand = String(number)
        } else if hand == "right" {
            result.append("R")
            rightHand = String(number)
        } else {
            result.append("L")
            leftHand = String(number)
        }
    }
    
    return result
}



let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
let hand = "right"

print(solution(numbers, hand))
