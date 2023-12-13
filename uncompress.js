const uncompress = (s) => {
  // Check if current char is number
    // If so, concat to temp
    // If not, concat to return string
  let tempNumStr = '';
  let returnStr = '';
  // Iterate through string
  for (let i = 0; i < s.length; i++) {
    if (!isNaN(s[i])) {
        console.log('here')
        console.log(s[i])
      tempNumStr += s[i];
      console.log(tempNumStr)
    } else {
      returnStr += s[i].repeat(Number(tempNumStr))
      console.log(returnStr)
      tempNumStr = '';
    }
  }
  return returnStr;
};

uncompress('2c3a1t')