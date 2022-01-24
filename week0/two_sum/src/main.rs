use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.read_line(&mut line);
    let numbers : Vec<u16> = line.split(" ").map(|e| String::from(e).parse().unwrap());
}