const compress = (s) => {
    // Check if current char is number
      // If so, concat to temp
      // If not, concat to return string
    let lead = 0;
    let trail = 0;
    let returnStr = '';
    // Iterate through chars
    for (let i = 0; i < s.length; i++) {
        lead = i;
        console.log(s[lead])
        console.log(s[trail])

        if (s[lead] !== s[trail]) {
            lead - trail === 1 ? 
                returnStr += `${s[trail]}` :
                returnStr += `${lead-trail}${s[trail]}`
            trail = i;
            console.log(s[lead])
            console.log(s[trail])
            console.log(returnStr)
            continue
        }
    }
    // Account for last characters
    lead++
    lead - trail === 1 ? 
            returnStr += `${s[trail]}` :
            returnStr += `${lead-trail}${s[trail]}`
    return returnStr;
  };
  
  console.log(compress('ssssbbz')) // -> 4s2bz