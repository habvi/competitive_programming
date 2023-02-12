fn get_sum(a: i32, b: i32) -> i32 {
    let mut x: i32 = a;
    let mut y: i32 = b;
    while y != 0 {
        let carry: i32 = (x & y) << 1;
        x ^= y;
        y = carry;
    }
    x
}

fn main() {
    println!("{}", get_sum(2, 3));
}
