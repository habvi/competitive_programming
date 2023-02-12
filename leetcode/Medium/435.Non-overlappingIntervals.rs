pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
    let mut vec: Vec<Vec<i32>> = intervals.iter().cloned().collect();
    vec.sort_by_key(|x| x[1]);

    let mut right: i32 = -50001;
    let mut ans: i32 = 0;
    for v in vec {
        let (start, end): (i32, i32) = (v[0], v[1]);
        if right <= start {
            right = end;
        } else {
            ans += 1;
        }
    }
    ans
}

fn main() {
    let intervals = vec![vec![1, 2], vec![3, 5], vec![1, 2]];
    println!("{}", erase_overlap_intervals(intervals));
}
