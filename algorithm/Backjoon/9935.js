/*문장을 처음부터 stack에 넣는다. stack 마지막 글자가 bomb의 마지막 글자와 같다면 그리고
bomb의 길이만큼까지와 단어가 같다면 splice 로 잘라준다. */

const input = require("fs").readFileSync("예제.txt").toString().trim().split("\n");

const stack = [];
const sentence = input[0]
const bomb = input[1];
const last_char = bomb[-1];
const bomb_len = bomb.length;

for (let i = 0; i < sentence.length; i++){
    stack.push(sentence[i]);
    if (stack[-1] == last_char && stack.slice(-bomb_len).join('') === bomb) {
    }    
}
const answer = stack.join('');
if (answer === '') {
    console.log('FRULA');
} else {
    console.log(answer);
}


