#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let firstMax = parseInt(process.argv[2]);
  let secondMax = parseInt(process.argv[3]);

  if (firstMax < secondMax) {
    [firstMax, secondMax] = [secondMax, firstMax];
  }

  for (let i = 4; i < process.argv.length; i++) {
    const currentNumber = parseInt(process.argv[i]);

    if (currentNumber > firstMax) {
      secondMax = firstMax;
      firstMax = currentNumber;
    } else if (currentNumber > secondMax) {
      secondMax = currentNumber;
    }
  }

  console.log(secondMax);
}
