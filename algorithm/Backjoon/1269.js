/* 대칭 차집합 원소의 개수를 출력하는 프로그램을 작성하시오.
두 배열에 대한 간단한 비교는 JSON.stringify를 통해 문자열로 변경해준 뒤 비교하는 방법 있다.
교집합,차집합 같은 경우엔 Array의 filter 와 includes.prototype.Method로 간단하게 비교할 수 있다.
교집합 : let intersection = arr1.filter(x => arr2.includes(x));
차집합 : let difference = arr1.filter(x => !arr2.includes(x));
*/

/*풀이법 생각 : 여집합을 구해서 length로 개수를 구하고 2번 빼주면 될 듯하다.
단순히 배열을 이용해 풀면 시간초과가 난다. 한 집합의 원소 최대원소개수가 20만개니까 20만곱하기20만 해서
시간복잡도가 너무 크다. 해쉬맵을 이용해 풀었다. */


let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = require('fs').readFileSync('예제.txt').toString().split('\n');

let count = input[0].split(' ');
let arr1 = input[1].split(' ');
let arr2 = input[2].split(' ');

const map1 = new Map();

for (let i = 0; i < arr1.length; i++){
    map1.set(arr1[i], arr1[i]);
}
let inter_count = 0;

for (let i = 0; i < arr2.length; i++){
    if (map1.get(arr2[i])) {
        inter_count++;
    }
};

console.log(Number(count[0]) + Number(count[1]) - (inter_count * 2));

