const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", function(line) {
    // 입력된 문자열의 공백을 제거한 후 공백을 기준으로 분리하여 배열을 만듭니다.
    const trimmedLine = line.trim();
    
    // 문자열이 비어 있으면 단어 개수는 0
    if (trimmedLine === '') {
        console.log("0");
    } else {
        const words = trimmedLine.split(/\s+/);
        console.log(words.length);
    }
    
    // readline 인터페이스를 종료합니다.
    rl.close();
}).on("close", function() {
    // 프로그램을 종료합니다.
    process.exit();
});
