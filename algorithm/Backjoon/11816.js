//정수 X 가 8진수, 10진수, 16진수 임의로 주어질 때 10진수로 바꿔서 출력하는 프로그램 작성해라.
// 한줄 입력이고, X는 10진수로 바꿨을 때 1,000,000 보다 작거나 같은 자연수다. 16진수 알파벳은 소문자로만이루어짐
// 8진수는 수 앞에 0 이 주어지고, 16진수는 0x 가 주어진다.

/*풀이법 10분 생각 : case를 3가지로 나눈다. 정수 X가 8,10,16 진수 일때. 0은 세케이스 모두에서 항상 0이고,
시작이 0 이고 뒤에 숫자가 없으면 0. 뒤에 숫자가 있으면 8진수이다. 뒤에 x가 오면 16진수다.
시작이 0이 아닌 숫자면 바로 10진수이다.
먼저 분기를 나누고 각 case별로 10진수로 바꾼다.
8진수나 16진수 일 경우에 뒤에서 부터 계산해야한다. 0승, 1승,2승,3승 다 더해줘야한다.
8 진수 : 01234567 , 16진수 : 0123456789abcdef
*/

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
// let input = fs.readFileSync("예제.txt").toString().split(" ");

let string_num = input[0]; // 하나의 string

function notation(string_num) {
  let str_num = string_num.split(""); // 각각의 배열로 담음
  let result = 0;
  if (str_num[0] !== "0") {
    return console.log(Number(string_num));
  } else {
    if (str_num.length === 1) {
      return console.log(0);
    }

    if (str_num[1] === "x") {
      console.log(parseInt(string_num, 16));
      //16진수 Number 쓰니까 자동 변환 되네????
      //   let count = 0;
      //   for (let i = str_num.length - 1; i >= 2; i--) {
      //     let trans_num;
      //     switch (str_num[i]) {
      //       case "a":
      //         trans_num = 10;
      //         break;
      //       case "b":
      //         trans_num = 11;
      //         break;
      //       case "c":
      //         trans_num = 12;
      //         break;
      //       case "d":
      //         trans_num = 13;
      //         break;
      //       case "e":
      //         trans_num = 14;
      //         break;
      //       case "f":
      //         trans_num = 15;
      //         break;

      //       default:
      //         trans_num = Number(str_num[i]);
      //         break;
      //     }
      //     result += (trans_num * (16**count));
      //     count++;
      //   }
      //   return result;
    } else {
      //8진수 는 0 사라지고 10이 남는다 이거만 잡자.
      console.log(parseInt(string_num, 8));

      //   let count = 0;
      //   for (let i = str_num.length - 1; i >= 1; i--) {
      //     result += (Number(str_num[i]) * (8 ** count));
      //     count++;
      //   }
      //   return result;
    }
  }
}

notation(string_num);
