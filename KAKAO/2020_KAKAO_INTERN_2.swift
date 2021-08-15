import Foundation

//let precedence = [ ["+" : 0, "-" : 1, "*": 2, "": -1],
//                   ["+" : 0, "*" : 1, "-": 2, "": -1],
//                   ["-" : 0, "+" : 1, "*": 2, "": -1],
//                   ["-" : 0, "*" : 1, "+": 2, "": -1],
//                   ["*" : 0, "+" : 1, "-": 2, "": -1],
//                   ["*" : 0, "-" : 1, "+": 2, "": -1]]

let precedence = [["+" : 0, "-" : 0, "*": 2, "": -1]]

extension Array {
    subscript (safe index: Int) -> Element? {
        return indices ~= index ? self[index] : nil
    }
    subscript(back i: Int) -> Element? {
        let backBy = i + 1
        return self[safe: self.index(self.endIndex, offsetBy: -backBy)]
    }
}

func convert(_ expression: String) -> [String] {
    var result: [String] = []
    var word = ""
    for character in expression {
        if Int(String(character)) != nil {
            word.append(character)
        } else {
            if !word.isEmpty {
                result.append(word)
            }
            result.append(String(character))
            word = ""
        }
    }
    if !word.isEmpty {
        result.append(word)
    }
    return result
}

func calculate(_ lhs: Int64, _ rhs: Int64, _ op: String) -> Int64? {
    switch op {
    case "+":
        return lhs + rhs
    case "*":
        return lhs * rhs
    case "-":
        return lhs - rhs
    default:
        return nil
    }
}

func solution(_ expression:String) -> Int64 {
    
    var maxResult: Int64 = 0
    let convertedExpr = convert(expression)
    for priority in precedence {
        var numberStack: [Int64] = []
        var operatorStack: [String] = []
        
        for word in convertedExpr {
        
            if let integer = Int64(word) {
                numberStack.append(integer)
                continue
            }
            
            let newOperator = word
            while priority[newOperator]! <= priority[operatorStack.last ?? ""]!, let rhs = numberStack[back: 0], let lhs = numberStack[back: 1], let op = operatorStack[back: 0], let result = calculate(lhs, rhs, op) {
                numberStack.removeLast()
                numberStack.removeLast()
                operatorStack.removeLast()
                numberStack.append(result)
            }
            operatorStack.append(newOperator)
        }
        while let rhs = numberStack[back: 0], let lhs = numberStack[back: 1], let op = operatorStack[back: 0], let result = calculate(lhs, rhs, op) {
            numberStack.removeLast()
            numberStack.removeLast()
            operatorStack.removeLast()
            numberStack.append(result)
        }
        maxResult = max(abs(numberStack.first ?? 0), maxResult)
    }
    return maxResult
}
let expression = "100-200*300-500+20"
let converted = convert(expression)


print(solution(expression))
