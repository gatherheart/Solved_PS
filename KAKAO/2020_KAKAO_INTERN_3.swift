import Foundation

func solution(_ gems:[String]) -> [Int] {
    var cache: [[Int]] = Array(repeating: Array(repeating: 1, count: gems.count), count: gems.count)
    var windows = Array(repeating: Array(repeating: Set<String>(), count: gems.count), count: gems.count)
    let kindsOfGems = Set(gems).count
    let numberOfGems = gems.count
    
    for i in 0..<numberOfGems {
        windows[i][i].insert(gems[i])
    }
    
    for length in 2...numberOfGems {
        for start in 0...numberOfGems-length {
            let end = start + length - 1
            let window = windows[start][end-1]
            if !window.contains(gems[end]) {
                cache[start][end] = cache[start][end-1] + 1
                windows[start][end] = window.union([gems[end]])
                if cache[start][end] == kindsOfGems {
                    print2DArray(cache)
                    return [start + 1, end + 1]
                }
                
            } else {
                cache[start][end] = cache[start][end-1]
                windows[start][end] = windows[start][end-1]
            }
        }
    }
    return [0, 0]
}

let gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
//let gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
