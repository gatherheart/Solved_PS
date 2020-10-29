const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  console.log(input);
  console.log("Hello Wolrd");
};

const input = [];
const start = function (rl) {
  rl.on("line", (line) => {
    input.push(line.split(" "));
  }).on("close", () => {
    solution(input);
    process.exit();
  });
};

console.log("Hello World");

start(rl);
