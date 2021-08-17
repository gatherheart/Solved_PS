import Foundation

func solution(_ gems:[String]) -> [Int] {
    var low = 0, high = 0
    let numberOfGems = gems.count
    let kindsOfGems = Set(gems).count
    var gemsCount = Dictionary<String, Int>()
    var candidates = Array<(Int, Int)>()
    
    while high < numberOfGems, low < numberOfGems {
        if kindsOfGems != gemsCount.count {
            gemsCount[gems[high], default: 0] += 1
            high += 1
        } else {
            candidates.append((low, high))
            gemsCount[gems[low], default: 0] -= 1
            if gemsCount[gems[low], default: 0] <= 0 {
                gemsCount[gems[low]] = nil
            }
            low += 1
        }
    }
    
    while kindsOfGems == gemsCount.count {
        candidates.append((low, high))
        gemsCount[gems[low], default: 0] -= 1
        if gemsCount[gems[low], default: 0] <= 0 {
            gemsCount[gems[low]] = nil
        }
        low += 1
    }
    
    let sorted = candidates.sorted { left, right -> Bool in
        if (left.1 - left.0) < (right.1 - right.0) {
            return true
        } else if (left.1 - left.0) == (right.1 - right.0) {
            return left < right
        } else {
            return false
        }
    }
        
    let result = sorted.first!
    return [result.0+1, result.1]
}
