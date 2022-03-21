/* 풀이법 생각 : 높은 수 부터 넣어가면서  숫자* 10**자릿수 + 숫자 를 N에서 빼가면서 일의자리까지 갔을때
0이 되면 찾은거다. 최소한으로 계산되도록 찾아보자.*/

const input = require("fs").readFileSync("/dev/stdin").toString().trim();

const num = Number(input);
const constructorArr = [];

// const num1 = input.split('');

// console.log(num1);
// console.log(num1.reduce((acc, num) => (acc += parseInt(num)), 0));

// function solution(n) {
//     const N = n.toString().split('');

//     return n + N.reduce((acc, num) => (acc += parseInt(num)), 0);
// }

// for (let i = 1; i <= num; i++){
//     if (solution(i) === num) {
//         constructorArr.push(i);
//     }
// }

// if (constructorArr.length) {
//     console.log(Math.min.apply(null, constructorArr));
// } else {
//     console.log(0);
// }

function solution(n) {
  let temp = n;
  let sum = n;

  while (temp) {
    sum += temp % 10;
    temp = parseInt(temp / 10);
  }

  return sum;
}

for (let i = 1; i <= num; i++) {
  if (solution(i) === num) {
    constructorArr.push(i);
  }
}

if (constructorArr.length) {
  console.log(Math.min.apply(null, constructorArr));
} else {
  console.log(0);
}

/* parseInt 잘써야하고, 생각하는 방식 흡수 해야한다. 1부터 num까지 다 함수로 보내서
맞는지 안맞는지 검사한다. solution(i) === num 이면 i는 num의 생성자이다. 여러 개일 수 있는 생성자, 혹은
없을 수 도 있는 생성자 판단해서 최소값 혹은 0 출력한다. */
