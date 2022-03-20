/* 배열 합치기 정렬이 되어 있는 두 배열 A,B 가 주어진다. 두 배열은 합친 다음 정렬해서 출력하는
프로그램 작성하시오. */

/*입력 : 1. 배열A의 크기 N, 배열 B의 크기 M.  1<= N,M <= 1,000,000)
        2. 배열 A의 내용
        3. 배열 B의 내용  둘 다 들어있는 수는 절댓값이 10**9 보다 작거나 같은 정수이다. */

/* 풀이법 생각 : 최대 100만번 계산으로 해결할 수 있을 듯 하나. 양쪽 배열에서 하나씩 꺼내서
비교 후 새로운 배열 만들기.. 이미 정렬이 되어있어서 앞에서만 빼면되서 상수에 시간복잡도를 가질것 같다.
투 포인터로 비교?? */

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = require('fs').readFileSync('예제.txt').toString().split('\n');

let count = input[0].split(' ');
let arrA = input[1].split(' ');
let arrB = input[2].split(' ');


let a_pointer = 0;
let b_pointer = 0;

let result = [];
while (a_pointer < arrA.length && b_pointer < arrB.length) {
    if (Number(arrA[a_pointer]) <= Number(arrB[b_pointer])) {
        result.push(arrA[a_pointer]);
        a_pointer++;
    }
    else {
        result.push(arrB[b_pointer]);
        b_pointer++;
    }
}

if (a_pointer !== arrA.length) {
    result.push(...arrA.slice(a_pointer));
}

if (b_pointer !== arrB.length) {
    result.push(...arrB.slice(b_pointer));
}

console.log(result.join(' '));