const pairProduct = (numbers, targetProduct) => {
    // Store arrays of index/num to be returned
    // If matching pair found
        // push index from diff and current element index 
        const diffs = {};
        let target;
        for (let i = 0; i <= numbers.length; i++) {
          // when we find matching pair, return out
          if (diffs[numbers[i]]) {
              return [diffs[numbers[i]].indexPos, i]
          } else {
              target = targetProduct / numbers[i]
              diffs[target] = {
                  val: target,
                  indexPos: i
              }
          }
        }
};

console.log(pairProduct([3, 2, 5, 4, 1], 8)); // -> [1, 3]