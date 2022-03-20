/* 단어에 숫자가 숨어있다. 이 숫자를 히든넘버. 알파벳 대/소문자와 숫자로 이루어진 단어가 주어졌을 때, 모든
히든 넘버의 합을 구하는 프로그램을 작성하라.
단어와 히든 넘버의 성질 : 연속된 숫자는 하나의 히든 넘버이다.
두 히든 넘버 사이에는 글자가 적어도 한 개 있다.
히든 넘버는 6자리를 넘지 않는다.

입력 첫째 줄 단어의 길이는 1<= n <= 5,000,000 이고 둘째 줄에 단어 주어짐. 단어는 알파벳 대/소문자 와 숫자(0~9)
*/

/* 풀이법 생각해보기
괄호 문제 풀듯이 풀 수 있을까? 숫자가 나올때 배열에 넣는 방식으로 풀 수 있을까? 스택이나 큐 처럼?
단어를 char 하나씩 배열로 바꾼다.처음부터 끝까지 한번 돈다. 숫자를 만나면, 빈 배열에 넣는다. 첫 숫자를 만난
후 부터 6번까지 히든넘버 가능하다. 숫자를 만나고 난 후 문자가 나온다면 그 동안 넣어뒀던 숫자 배열을 하나의 연속된
숫자로 바꾼다. 결과값에 더한다. 그 다음 계속 for문을 돈다. string 타입 단어가 숫자인지 문자인지 판별할 수 있나?
문자를 다 Number로 바꾸고 number아닌애들 뺄까? 
문자 Number변환 하면 NaN 값 나온다. 이걸 이용해볼까?*/

// 이렇게 문제 조건 자체를 함수로 만들어서 넘겨주면서 테스트 해볼수 있네.. 하나 배움.
// function createRandomString(length = 5) {
    //   let text = ""
    //   const possible =
    //     "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    //   Array.from(Array(length)).forEach(() => {
    //     text += possible.charAt(Math.floor(Math.random() * possible.length))
    //   })
    //   return text
    // }
    
    // const str = createRandomString(5000000)



let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = require("fs").readFileSync("예제.txt").toString().split("\n");

let count = input[0];
let hiddenNum = input[1].split("");

function result(count, hiddenNum) {
  let result = [];
  let num_sum = 0;
  for (let i = 0; i < count; i++) {
    if (!isNaN(Number(hiddenNum[i]))) {
      result.push(hiddenNum[i]);
    } else {
      if (result.length !== 0) {
        num_sum += Number(result.join(""));
        result = [];
      } else {
        continue;
      }
    }
  }
  if (result.length !== 0) {
    num_sum += Number(result.join(""));
  }
  console.log(num_sum);
}

result(count, hiddenNum);
