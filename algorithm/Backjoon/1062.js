/* 남극의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다.
어떤 K단어만 가르쳤을때 학생들이 읽을 수 있는 단어의 최대 갯수를 구하는 프로그램 작성하시오. */

/* 입력
1. 남극단어의 갯수 N, 가르친 글자 K 주어진다. (1 <= N <= 50), (0 <= K <= 26) 이다.
2. 둘 째줄 부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고,
    (8<= 단어.length <= 15) , 중복은 없다.

    출력
1. 단어 갯수 최댓값 출력
*/

/* 10분 풀이 생각 : a,n,t,i,c 는 무조건 배워야한다. 아니면 한글자도 못 읽음. K는 5개는 무조건 넘어야한다.
주어지는 단어들에서 a,n,t,i,c를 뺐을 때 남은 글자들 중 몇개를 배워야 할까? 문자열 인덱스 0~3 까지 -1~-3까지는
제외하고 문자를 봐야한다.*/

let fs = require("fs");
let input = fs.readFileSync("test.txt").toString().split("\n");

let wordCount = parseInt(input[0].split(" ")[0]);
let studyWordCount = parseInt(input[0].split(" ")[1]);
let words = input.slice(1);

function solution(wordCount, studyWordCount, words) {
  if (studyWordCount < 5) return 0;
  for (let i = 0; i < words.length; i++){
    let word = words[i];
    console.log(word.slice(0, 4));
    console.log(word.slice(-4));
  }
}

// console.log(solution(wordCount, studyWordCount, words));
solution(wordCount, studyWordCount, words);

