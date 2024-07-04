// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		
	//console.log('Hello Goorm! Your input is', line);
		const arr = line.split(' ');
		let sum = 0;
		for(let i=0;i<arr.length;i++){
			sum += Number(arr[i]);
		}
		console.log(sum);
		rl.close();
	}
	
	process.exit();
})();
