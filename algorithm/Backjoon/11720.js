let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
// let input = fs.readFileSync("예제.txt").toString().split("\n");

let count = input[0];
let string_numbers = input[1];


function add(count, string_numbers) {
  let str_num = string_numbers.split("");

  let result = 0;

  for (let i = 0; i < count; i++) {
    result += Number(str_num[i]);
  }

  return result;
}

console.log(add(count, string_numbers));

/* n개의 숫자 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램 작성해라.
 첫째 줄에 숫자의 개수 1<= N <=100, 둘째 줄에 숫자 N개가 공백없이 주어진다.
 풀이법 생각 : 숫자는 0 ~ 9 일것이다. n만큼 덧셈을 하면 된다. 최초 result를 0으로 두고 더하자
 공백없는 숫자를 어떻게 나누어서 구할 것이냐.
 문자열로 입력 받고 split해서 나누자.*/
