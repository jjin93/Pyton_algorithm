/* 새로운 블랙잭, 각 카드는 양의 정수. 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다..
그런후 딜러는 숫자 M을 외친다. 플레이어는 제한된 시간안에 N장의 카드중 3장을 고른다.
플레이어가 고른 카드의 합은 M을 넘지않으면서 M과 최대한 가깝게 만들어야한다.
N장의 카드 숫자 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드3장의 합을 구해 출력하시오. */

/* 입력 : 
1. 카드의 개수 N(3 <= N <=100), M(10<= M <= 300,000)이 주어진다.
2. 카드에 쓰여있는 수. 이 값은 100,000을 넘지 않는 양의 정수이다.(합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 있다)
    출력 :
    1. 카드 3장의 합
    */

/*10분 풀이생각 : 3장 고르기니까 경우의 수 100*99*98이다.계산할만하다 일일이 다 해보자.
*/

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let [N, M] = input[0].split(' ');
N = parseInt(N);
M = parseInt(M);

let select_card = input[1].split(' ');

let max = 0;

const dfs = (select_card, num, arr = []) => {
    if (num === 3) {
        arr = arr.map(value => parseInt(value));
        let reducer = (acc, curr) => acc + curr;
        let sum = arr.reduce(reducer);
        if (sum > max && sum <= M) {
            max = sum;
        }
    }
    else {
        for (let i = 0; i < select_card.length; i++) {
            arr.push(select_card[i]);
            dfs(select_card.slice(i + 1), num + 1, arr);
            arr.pop();
        }
    }
};

dfs(select_card, 0);
console.log(max);