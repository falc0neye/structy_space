// const pairSum = (numbers, targetSum) => {
//     // Store arrays of index/num to be returned
//     // If matching pair found
//         // push index from diff and current element index 
//   const diffs = {};
//   let curr;
//   numbers.forEach((num, index) => {
//     console.log(num)
//     console.log(diffs)
//     currDiff = targetSum - num;
//     console.log(currDiff);
//     // First check if curr number is in diffs
//     if (diffs[num]) {
//         console.log('here')
//         console.log(num)
//         return [diffs[target - num].index, index]
//     }
//     else {
//         console.log('here', currDiff)
//         diffs[currDiff] = {
//             val: currDiff,
//             index: index
//         }
//     } 
//     console.log(num);
//   })
// };

const pairSum = (numbers, targetSum) => {
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
        target = targetSum - numbers[i]
        diffs[target] = {
            val: target,
            indexPos: i
        }
    }
  }
};

console.log(pairSum([3, 2, 5, 4, 1], 8)); // -> [0, 2]