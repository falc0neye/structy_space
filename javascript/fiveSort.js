const fiveSort = (nums) => {
    let currIndex = nums.length - 1;
    let temp;
    for (let i = 0; i < nums.length; i++) {
        // console.log(nums[i])
        // console.log(nums[currIndex])
        // temp = i;
        if (currIndex <= i) break;
        if (nums[i] === 5) {
            while (nums[currIndex] === 5) currIndex--;
            // console.log(nums[i])
            // console.log(nums[currIndex])
            temp = nums[currIndex];
            nums[currIndex] = nums[i];
            nums[i] = temp;
            currIndex--
        }
    }
    return nums;
  };

  console.log(fiveSort([12, 5, 1, 5, 12, 7]));
  console.log(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))