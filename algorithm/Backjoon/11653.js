let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

let num = Number(input);
// let num = 72;

function solution(n) {
  let arr = Array(n + 1)
    .fill(true)
    .fill(false, 0, 2);

  let result = n;
  for (let i = 2; i <= n; i++) {
    if (arr[i]) {
      while (result % i === 0) {
        result = result / i;
        console.log(i);
      }

      for (let j = i * i; j <= n; j += i) {
        arr[j] = false;
      }
    }
  }
}

solution(num);
