fn find_pali(s: &Vec<char>, i: i32, j: i32, n: i32, ans: &mut i32) -> () {
    let mut left = i;
    let mut right = j;
    while 0 <= left && right < n {
        if s[left as usize] != s[right as usize] {
            break;
        }
        *ans += 1;
        left -= 1;
        right += 1;
    }
}

fn count_substrings(s: String) -> i32 {
    let s: Vec<char> = s.chars().collect();
    let n: i32 = s.len() as i32;
    let mut ans: i32 = 0;
    for mid in 0..n {
        find_pali(&s, mid, mid + 1, n, &mut ans);
        find_pali(&s, mid, mid, n, &mut ans);
    }
    ans
}

fn main() {
    let s = String::from("aaa");
    println!("{}", count_substrings(s));
}
