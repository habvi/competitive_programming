use std::process::exit;

fn longest_common_subsequence(text1: String, text2: String) -> i32 {
    use std::cmp::max;
    let s: Vec<char> = text1.chars().collect();
    let t: Vec<char> = text2.chars().collect();
    let len_1 = s.len();
    let len_2 = t.len();
    let mut dp: Vec<Vec<usize>> = vec![vec![0; len_2 + 1]; len_1 + 1];
    for i in 0..(len_1 + 1) {
        for j in 0..(len_2 + 1) {
            if i < len_1 && j < len_2 && s[i] == t[j] {
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1);
            }
            if i < len_1 {
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
            }
            if j < len_2 {
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j]);
            }
        }
    }
    dp[len_1][len_2] as i32
}

fn main() {
    let text1 = String::from("abcde");
    let text2 = String::from("ace");
    println!("{}", longest_common_subsequence(text1, text2));
}
