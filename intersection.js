const a = [];
const b = [];
for (let i = 0; i < 50000; i += 1) {
  a.push(i);
  b.push(i);
}

const intersection = (a, b) => {
    // use same pointer to check if elements in one array are in the other
    const returnArr = [];
    const cache = {};
    if (a.length <= b.length) {
        a.forEach(el => {
            if (!cache[el]) {
                cache[el] = el;
            }
        })
    } else {
        b.forEach(el => {
            if (!cache[el]) {
                cache[el] = el;
            }
        })
    }

    if (a.length <= b.length) {
        b.forEach(el => {
            if (cache[el]) {
                returnArr.push(el)
            }
        })
    } else {
        a.forEach(el => {
            if (cache[el]) {
                returnArr.push(el)
            }
        })
    }

    return returnArr;
  };

//   console.log(intersection([4,2,1,6], [3,6,9,2,10])) // -> [2,6]

  console.log(intersection(a, b)) // -> [0,1,2,3,..., 49999]