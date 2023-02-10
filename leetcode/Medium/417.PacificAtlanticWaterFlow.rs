use std::collections::VecDeque;

const DXY: [[i32; 2]; 4] = [[0, 1], [1, 0], [0, -1], [-1, 0]];

fn bfs(heights: &Vec<Vec<i32>>, seen: &mut Vec<Vec<bool>>, sy: usize, sx: usize, h: usize, w: usize) -> () {
    seen[sy][sx] = true;
    let mut que: VecDeque<(usize, usize)> = VecDeque::new();
    que.push_back((sy, sx));
    while que.len() != 0 {
        let (y, x): (usize, usize) = que.pop_front().unwrap();
        for [dy, dx] in DXY {
            let (ny, nx): (i32, i32) = (y as i32 + dy, x as i32 + dx);
            if !(0 <= ny && ny < h as i32 && 0 <= nx && nx < w as i32) {
                continue;
            }
            let (ny, nx): (usize, usize) = (ny as usize, nx as usize);
            if seen[ny][nx] == true {
                continue;
            }
            if heights[ny][nx] < heights[y][x] {
                continue;
            }
            seen[ny][nx] = true;
            que.push_back((ny, nx));
        }
    }
}

fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let h: usize = heights.len();
    let w: usize = heights[0].len();
    let mut pacific: Vec<Vec<bool>> = vec![vec![false; w]; h];
    for i in 0..h {
        for j in 0..w {
            if (i == 0 || j == 0) && !pacific[i][j] {
                bfs(&heights,&mut pacific, i, j, h, w);
            }
        }
    }
    let mut atlantic: Vec<Vec<bool>> = vec![vec![false; w]; h];
    for i in 0..h {
        for j in 0..w {
            if (i == h - 1 || j == w - 1) && !atlantic[i][j] {
                bfs(&heights,&mut atlantic, i, j, h, w);
            }
        }
    }
    let mut ans: Vec<Vec<i32>> = Vec::new();
    for i in 0..h {
        for j in 0..w {
            if pacific[i][j] && atlantic[i][j] {
                ans.push(vec![i as i32, j as i32])
            }
        }
    }
    ans
}

fn main() {
    let heights = vec![vec![1, 2, 2, 3, 5], vec![3, 2, 3, 4, 4], vec![2, 4, 5, 3, 1], vec![6, 7, 1, 4, 5], vec![5, 1, 1, 2, 4]];
    println!("{:?}", pacific_atlantic(heights));
}
